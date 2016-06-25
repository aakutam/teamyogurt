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
var exec = require('child_process').execFile;
var tesseract = require('node-tesseract');

app.get('/',function(req,res){
      res.sendFile(__dirname + "/index.html");
});

app.post('/api/photo',function(req,res){
    upload(req,res,function(err) {
        if (err) {
            console.log(err)
            return res.end("Error uploading file.");
        }
	const filename = req.file.originalname;
	const options = {
	    l: 'eng'
	}
	tesseract.process(__dirname + '/uploads/' + filename, options, function(err, text) {
	
	    if (err) {
		console.log(err);
	    } else {
		console.log(text);
	    }
	});

    });
});

app.listen(80, function(){
    console.log("Working on port 80");
});
