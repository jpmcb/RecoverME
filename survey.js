//-----------------------------------------------------------------------------
// Description: This file contains the definition for the Survey and Question
//                class.
//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------
// Defines an interface for a survey.
//      questionList = an array of Question objects
//      userId = identifier to store results of each user
//-----------------------------------------------------------------------------
class Survey {
    constructor(questions, userId) {
        this.questionList = questions;
        this.userId = userId;
    }

    get questions() {
        return this.questionList;
    }

    get user() {
        return this.userId;
    }

    // send results to backend/DB
    logResults() {
        // TODO
    }
}

//-----------------------------------------------------------------------------
// Defines an interface for a survey.
//      text = the text string of the question being asked
//      answerOptions = different options the user is presented with for
//                      answering the question.
//      usrAnswer = the answer the user chose
//-----------------------------------------------------------------------------
class Question {
    constructor(qtext, answers){
        this.text = qtext;
        this.answerOptions = answers;
        this.usrAnswer;
    }

    get questionText() {
        return this.text;
    }

    set questionText(qtext) {
        this.text = qtext;
    }

    get answerSet() {
        return this.answerOptions;
    }

    set answerSet(ans) {
        this.answerOptions = ans;
    }

    get userAnswer() {
        return this.usrAnswer;
    }

    set userAnswer(answer){
        if (this.answerSet.indexOf(answer) > -1) {
            this.usrAnswer = answer;
        }
        else {
            throw("Error: Invalid answer for this question. Try again.");
        }
    }
}

module.exports  = {
    Survey,
    Question
}