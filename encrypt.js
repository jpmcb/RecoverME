// CS 361 - Software engineering
// RecoverME 
// ---------
// Description: Password encryption module. Can be used
//      to convert plain text passwords into special hashes

var crypto = require('crypto');
var bcrypt = require('bcrypt');

// Number of times to salt the hash
const saltRounds = 10;

// Converts plaintext --> hash
var getPassword = function(plaintext, callback){
    bcrypt.genSalt(saltRounds, function(err, salt){
        bcrypt.hash(plaintext, salt, function(err, hash){
            if(err) throw err;
          
            callback(hash);
        });
    });
}

// Checks if plaintext password == hash 
var checkPassword = function(plaintext, hash, callback){
    bcrypt.compare(plaintext, hash, function(err, res){
        callback(res);
    });
}

module.exports = {
    getPassword: getPassword,
    checkPassword: checkPassword
};