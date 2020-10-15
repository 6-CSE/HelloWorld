var express = require('express');

var app = express();

app.set('view engine','ejs');

app.get('/',function(req,res){
	res.sendFile(__dirname + '/views/index.html');
});

app.get('/contact',function(req,res){
	res.send('Cotac page is called');
});

app.get('/profile/:name',function(req,res){
	var data = {age: 35 , job: 'clerk'};
	res.render('profile', {person : req.params.name, data : data});
});

app.listen(3000);