// CS 361 - Software engineering
// RecoverME 
// ---------
// Description: Unit testing file
//      Executed by the Travis CI integrated testing API

var assert = require('assert');

var encrypt = require('./encrypt.js');
var Survey = require('./survey.js');

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

///-----------------------------------------------------------------------------
// Survey tests - actually running them
//-----------------------------------------------------------------------------/
surveyTestSuite();

//-----------------------------------------------------------------------------
// Runs all the tests for the Survey and Question class
//-----------------------------------------------------------------------------
function surveyTestSuite() {
    let userId = 100;
    let questionInfo =  {
        q1: {
            text: "Who's the best?",
            answer: ["Ron Swanson", "Leslie Knope", "April Ludgate", "Andy Dwyer", "Tom Haverford"]
        },
        q2: {
            text: "Do you lift?",
            answer: ["Yes", "No"]
        }
    };
    // set up instances for testing
    let testQuestion1 = new Survey.Question(questionInfo.q1.text, questionInfo.q1.answer);
    let testQuestion2 = new Survey.Question(questionInfo.q2.text, questionInfo.q2.answer);
    let questionList = [testQuestion1, testQuestion2];

    // test question set up
    testQuestionSetUp(questionInfo.q1);

    // test recording answer
    testQuestionUserAnswer(testQuestion1, "Ron Swanson", true);     
    testQuestionUserAnswer(testQuestion1, "Ben Wyatt", false);     

    // test survey set up
    testSurveyQuestions(questionList, userId);

    console.log("Survey tests complete. If no error messages, passed");
}

//-----------------------------------------------------------------------------
// Tests the intitalization and getters of the questions in the Question class
//-----------------------------------------------------------------------------
function testQuestionSetUp(q1) {
    let testQuestion1 = new Survey.Question(q1.text, q1.answer);

    if (testQuestion1.questionText != "Who's the best?"){
        console.error("ERROR: testQuestionSetUp - Question initialization and fetching failed");
    }

    if (!equalArrays(testQuestion1.answerSet,   ["Ron Swanson", 
                                                 "Leslie Knope", 
                                                 "April Ludgate",
                                                 "Andy Dwyer", 
                                                 "Tom Haverford"]
                                                )
                                            ){
        console.error("ERROR: testQuestionSetUp - Question ANSWER initialization and fetching failed");
    }

    // Validates that array a is equivalent to array b
    function equalArrays(a, b) {
        if (a.length != b.length) return false;

        for (let i = 0; i < a.length; i++) {
            if (a[i] !== b[i]) return false;
        }
        return true;
    }
}

//-----------------------------------------------------------------------------
// Tests the intitalization and getters of the answers in the Question class
//-----------------------------------------------------------------------------
function testQuestionUserAnswer(questionInstance, selection, valid) {
    if (valid) {
        questionInstance.userAnswer = selection;
        if (questionInstance.userAnswer !== selection) {
            console.error("ERROR: testQuestionUserAnswer - Recording user answer failed");
        }
    }
    else {
        try {
            questionInstance.userAnswer = selection;
            console.error("ERROR: testQuestionUserAnswer - Invalid answer input not caught");
        } 
       catch(e){} // do nothing, successfully threw error
    }
}

//-----------------------------------------------------------------------------
// Tests the intitalization and getters of the Survey class
//-----------------------------------------------------------------------------
function testSurveyQuestions(questions, id) {
    let testSurvey = new Survey.Survey(questions, id);
    surveyQuestions = testSurvey.questions;

    if (surveyQuestions !== questions) {
        console.error("ERROR: testSurveyQuestions - Survey questions failed to set up correctly.");
    }

    if (testSurvey.user !== id) {
        console.error("ERROR: testSurveyQuestions - Survey user ID failed to set up.");
    }
}

