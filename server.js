// CS 361 - Software engineering
// RecoverME 
// ---------
// Description: Node JS entry point


// Include the needed middleware
var express = require('express');
var handlebars = require('express-handlebars').create({defaultLayout: 'main'});
var bodyParser = require('body-parser');
var fs = require('fs');

// Build the application
var app = express();

// For the path to the public folder in the express fild tree
app.use(express.static('public'));

// set up the application
app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', process.env.PORT || 3000); // TODO - Change on engineering server

// set up the body parser middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// ---------------
// The GET request for the web app
// ---------------
app.get('/', function(req, res){
    // Send to the home page
    res.render('home');
});

app.get('/home', function(req, res){
    res.render('home');
});

app.get('/survey', function(req, res){
    res.render('survey');
});

app.post('/survey', function(req, res){
    console.log(req.body);

    // var payload = {};
    // var params = [];
    


    // console.log(params);

    // payload.results = params;

    res.render('survey', req.body);
})

// -------------------------
// --- Server functions ----
// -------------------------

// The route (404) error handler
app.use(function(req, res){
    res.status(404);
    res.render('404');
});

// The server (500) error handler
app.use(function(err, req, res, next){
    console.error(err.stack);
    res.status(500);
    res.render('500');
});

// Start the application on the specified port (port 3000 for local development)
app.listen(app.get('port'), function(){
    console.log('Express started on port:' + app.get('port'));
});