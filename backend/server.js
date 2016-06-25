var express =   require("express");
var multer  =   require('multer');
var app     =   express();
var storage =   multer.diskStorage({
  destination: function (req, file, callback) {
    callback(null, './uploads');
  },
  filename: function (req, file, callback) {
    console.log(file)
    callback(null, file.originalname);
  }
});
var upload = multer({ storage : storage}).single('userPhoto');
var exec = require('child_process').exec;

app.get('/',function(req,res){
      res.sendFile(__dirname + "/index.html");
});

app.post('/api/photo',function(req,res){
    console.log(req)
    upload(req,res,function(err) {
        if (err) {
            console.log(err)
            return res.end("Error uploading file.");
        }
	const filename = req.file.originalname;
	const options = {
	    maxBuffer: 2000 * 1024
	};
	exec('python ../classify/classifyImg.py ' + filename, options, function(err, stdout, stderr) {
	    if (err) {
		console.log(err);
	    } else {
		console.log("What's the problem");
		console.log(stdout);
		res.send(stdout);
	    }
	})
    });
});

app.listen(80, function(){
    console.log("Working on port 80");
});
