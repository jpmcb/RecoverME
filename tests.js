// CS 361 - Software engineering
// RecoverME 
// ---------
// Description: Unit testing file
//      Gets executed by the Travis CI integrated testing API

var assert = require('assert');

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