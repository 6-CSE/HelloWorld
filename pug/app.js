const express = require("express");
const path = require('path');
const app = express();
const port = 80;


// EXPRESS SPECIFIC STUFF
app.use('/static', express.static('static')); // For serving static files
app.use(express.urlencoded()); 

// PUG SPECIFIC STUFF
app.set('view engine', 'pug') // Set the template engine as pug
app.set('views', path.join(__dirname, 'views')); // Set the views directory
 
// ENDPOINTS
app.get('/', (req, res)=>{
    const params = { };
    res.status(200).render('hello.pug', params);
});
app.get('/hi', (req, res)=>{
    const params = { };
    res.status(200).render('hi.pug', params);
});
app.get('/hey', (req, res)=>{
    const params = { };
    res.status(200).render('hey.pug', params);
});
app.get('/contact', (req, res)=>{
    const params = { };
    res.status(200).render('contact.pug', params);
});


// START THE SERVER
app.listen(port, ()=>{
    console.log(`The application started successfully on port ${port}`);
});
