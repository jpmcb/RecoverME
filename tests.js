// CS 361 - Software engineering
// RecoverME 
// ---------
// Description: Unit testing file
//      Executed by the Travis CI integrated testing API

var assert = require('assert');

var encrypt = require('./encrypt.js');

// Simple addition function
function addTwo(x, y){
    return x + y;
}

// Simple unit test for the addition function
function testAddTwo(){
    var x = 5;
    var y = 1; 
    var sum1 = addTwo(x, y);
    var sum2 = x + y;

    console.log('addTwo() should return ' + sum1 + ' equal ' + sum2);

    try{
        assert.equal(sum1, sum2);
        console.log('Passed.');
    } catch (error) {
        console.error('Failed.');
    }
}

// Initiate the addition function
testAddTwo();


// ------------------
// Password encryption unit tests
// ------------------
var saved_hash;

// Simple plain text password
encrypt.getPassword("helloworld", function(hash){
    saved_hash = hash;
    encrypt.checkPassword("helloworld", saved_hash, function(res){
        if(res == true)
            console.log('Password encryption Passed!');
        else
            console.error('Password encryption Failed!');
    });
});

// All letters and numbers
encrypt.getPassword("abcdefghijklmnopqrstuvwxyz1234567890", function(hash){
    saved_hash = hash;
    encrypt.checkPassword("abcdefghijklmnopqrstuvwxyz1234567890", saved_hash, function(res){
        if(res == true)
            console.log('Password encryption Passed!');
        else
            console.error('Password encryption Failed!');
    });
});

// Special characters test
encrypt.getPassword("!@#$%^&**()-=+_[]{};:<>?,.", function(hash){
    saved_hash = hash;
    encrypt.checkPassword("!@#$%^&**()-=+_[]{};:<>?,.", saved_hash, function(res){
        if(res == true)
            console.log('Password encryption Passed!');
        else
            console.error('Password encryption Failed!');
    });
});