const express = require('express');
const app = express();
const {exec, execSync} = require('child_process');

const port = 3001;

app.set('views', './views');
app.set('view engine', 'ejs');

app.use(express.static(__dirname+'/public'));

app.get('/', function(req, res) {
    res.render('index.ejs');
});

app.get('/lipreader', function(req, res) {
    res.render('lipreader.ejs');
});

app.get('/python', function(req, res) {
    var proc = exec('python public/temp.py', function(err, stdout, stderr) {
        if(err) {console.log('Child process error: ', err);}
        else {
            console.log(stdout);
            console.log(stderr);
        }
        res.send(stdout);
    });
});

app.listen(port, function(err) {
    if(err) {console.log('Could not connect to the server: ', err);}
    else {console.log('Connected to server! on port: ', port);}
});