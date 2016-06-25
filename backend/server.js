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

app.get('/',function(req,res){
      res.sendFile(__dirname + "/index.html");
});

app.post('/api/photo',function(req,res){
    upload(req,res,function(err) {
        if (err) {
            console.log(err)
            return res.end("Error uploading file.");
        }
	var filename = req.file.originalname;
	exec('./test.sh',['-o'], function(error, stdout, stderr) {
            if (error) return error;
            else {
                res.end(stdout);
            }
        });
    });
});

app.listen(3000,function(){
    console.log("Working on port 3000");
});
