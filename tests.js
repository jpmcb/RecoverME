var assert = require('assert');

function addTwo(x, y){
    return x + y;
}

function testAddTwo(){
    var x = 5;
    var y = 1; 
    var sum1 = addTwo(x, y);
    var sum2 = x + x;

    console.log('addTwo() should return ' + sum1 + ' equal ' + sum2);

    try{
        assert.equal(sum1, sum2);
        console.log('Passed.');
    } catch (error) {
        console.error('Failed.');
    }
}

testAddTwo();