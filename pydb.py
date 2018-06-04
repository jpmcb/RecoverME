#!/usr/bin/env python
import sys


class User :
    def __init__(self, user_id, user_type, user_location) :
        self.user_id = user_id
        #self.user_location = user_location
        self.user_state = user_location[0]
        self.user_city = user_location[1]
        self.user_type = user_type

class Link :
    def __init__(self, link_id, url, user_type = 0) :
        self.link_id = link_id
        self.url = url
        self.user_type = user_type



class Clinic :
    def __init__(self, clinic_id, name, clinic_rating, clinic_phone, clinic_state, clinic_city, clinic_specialty, clinic_url) :
        self.clinic_id = clinic_id
        self.clinic_name = name
        self.clinic_rating = clinic_rating
        self.clinic_phone = clinic_phone
        self.clinic_state = clinic_state
        self.clinic_city = clinic_city
        self.clinic_specialty = clinic_specialty
        self.clinic_url = clinic_url


class Question :
    def __init__(self, question_id, question, choices) :
        self.choices = []
        self.question_id = question_id
        self.question = question
        for i in choices :
            self.choices.append(i)

    def evaluate_questionnaire(responses) :
        User(user_id, responses[0], responses [1], responses [2])
        if(responses[0] == 1) :
            return "struggling with addiction";
        if(answer_list[0] == 2) :
            return "at risk addiction"
        if(answer_list[0] == 3) :
            return "friend"
        if(answer_list[0] == 4) :
            return "family"

class Questionnaire :
    def __init__(self, Questionnaire_Id, Reponses) :
        self.Id = Questionnaire_Id
        self.Responses = []

class Database :
    def __init__(self, Links, Clinics, Questions, Users) :
        self.Link_list = []
        self.Question_list = []
        self.User_list = []
        self.Clinic_list = []
        for i in Links :
            self.Link_list.append(i)
        for i in Clinics :
            self.Clinic_list.append(i)
        for i in Questions :
            self.Question_list.append(i)
        for i in User_list :
            self.User_list.append(i)

    def insert_into_users(self, user_id, user_location, user_type) :
        self.User_list.append(User(user_id, user_location, user_type));
    def insert_into_links(self, link_id, url, user_type) :
        self.Link_list.append(Link(link_id, url, user_type));
        print "Appending"
    def insert_into_questions(self, question_id, question, choices) :
        self.Question_list.append(Question(question_id, question, choices));
    def insert_into_clinics(self, clinic_id, name, clinic_rating, clinic_phone, clinic_state, clinic_city, clinic_specialty, clinic_url) :
        self.Clinic_list.append(Clinic(clinic_id, name, clinic_rating, clinic_phone, clinic_state, clinic_city, clinic_specialty, clinic_url));

    def select_from_users(self, field, value) :
        retval = []
        if field == "user_id" :
            for i in User_list :
                if i.user_id == value :
                    retval.append(str(i.user_id))
                    retval.append(str(i.user_type))
                    retval.append(str(i.user_state))
                    retval.append(str(i.user_city))
            return retval
        elif field == "user_type" :
            for i in User_list :
                if i.user_type == value :
                    retval.append(str(i.user_id))
                    retval.append(str(i.user_type))
                    retval.append(str(i.user_state))
                    retval.append(str(i.user_city))
            return retval
        elif field == "user_state" :
            for i in User_list :
                if i.user_state == value :
                    retval.append(str(i.user_id))
                    retval.append(str(i.user_type))
                    retval.append(str(i.user_state))
                    retval.append(str(i.user_city))
            return retval
        elif field == "user_city" :
            for i in User_list :
                if i.user_city == value :
                    retval.append(str(i.user_id))
                    retval.append(str(i.user_type))
                    retval.append(str(i.user_state))
                    retval.append(str(i.user_city))
            return retval
        else :
            return "Error. Users does not have a property " + str(field) + ".";

    def select_from_links(self, field, value) :
        retval = []
        if field == "link_id" :
            for i in Link_list :
                if i.link_id == value :
                    retval.append(str(i.link_id))
                    retval.append(str(i.url))
                    retval.append(str(i.user_type))
            return retval
        elif field == "url" :
            for i in Link_list :
                if i.url == value :
                    retval.append(str(i.link_id))
                    retval.append(str(i.url))
                    retval.append(str(i.user_type))
            return retval
        elif field == "user_type" :
            for i in Link_list :
                if i.user_type == value :
                    retval.append(str(i.link_id))
                    retval.append(str(i.url))
                    retval.append(str(i.user_type))
            return retval
        else :
            return "Error. Links does not have a propery " + str(field) + ".";

    def select_from_questions(self, field, value) :
        retval = []
        if field == "question_id" :
            for i in Question_list :
                if i.question_id == value :
                    retval.append(str(i.question_id))
                    retval.append(str(i.question))
            return retval
        elif field == "question" :
            for i in Question_list :
                if i.question == value :
                    retval.append(str(i.question_id))
                    retval.append(str(i.question))
            return retval
        else :
            return "Error. questions does not have a propery " + str(field) + ".";

    def select_from_clinics(self, field, value) :
        retval = []
        if field == "clinic_id" :
            for i in Clinic_list :
                if i.clinic_id == value :
                    retval.append(str(i.clinic_id))
                    retval.append(str(i.clinic_name))
                    retval.append(str(i.clinic_rating))
                    retval.append(str(i.clinic_phone))
                    retval.append(str(i.clinic_state))
                    retval.append(str(i.clinic_city))
                    retval.append(str(i.clinic_specialty))
                    retval.append(str(i.clinic_url))
            return retval
        elif field == "clinic_name" :
            for i in Clinic_list :
                if i.clinic_name == value :
                    retval.append(str(i.clinic_id))
                    retval.append(str(i.clinic_name))
                    retval.append(str(i.clinic_rating))
                    retval.append(str(i.clinic_phone))
                    retval.append(str(i.clinic_state))
                    retval.append(str(i.clinic_city))
                    retval.append(str(i.clinic_specialty))
                    retval.append(str(i.clinic_url))
            return retval
        elif field == "clinic_rating" :
            for i in Clinic_list :
                if i.clinic_rating == value :
                    retval.append(str(i.clinic_id))
                    retval.append(str(i.clinic_name))
                    retval.append(str(i.clinic_rating))
                    retval.append(str(i.clinic_phone))
                    retval.append(str(i.clinic_state))
                    retval.append(str(i.clinic_city))
                    retval.append(str(i.clinic_specialty))
                    retval.append(str(i.clinic_url))
            return retval
        elif field == "clinic_phone" :
            for i in Clinic_list :
                if i.clinic_phone == value :
                    print "appending"
                    retval.append(str(i.clinic_id))
                    retval.append(str(i.clinic_name))
                    retval.append(str(i.clinic_rating))
                    retval.append(str(i.clinic_phone))
                    retval.append(str(i.clinic_state))
                    retval.append(str(i.clinic_city))
                    retval.append(str(i.clinic_specialty))
                    retval.append(str(i.clinic_url))
            return retval
        elif field == "clinic_state" :
            for i in Clinic_list :
                if i.clinic_list == value :
                    retval.append(str(i.clinic_id))
                    retval.append(str(i.clinic_name))
                    retval.append(str(i.clinic_rating))
                    retval.append(str(i.clinic_phone))
                    retval.append(str(i.clinic_state))
                    retval.append(str(i.clinic_city))
                    retval.append(str(i.clinic_specialty))
                    retval.append(str(i.clinic_url))
            return retval
        elif field == "clinic_city" :
            for i in Clinic_list :
                if i.clinic_city == value :
                    retval.append(str(i.clinic_id))
                    retval.append(str(i.clinic_name))
                    retval.append(str(i.clinic_rating))
                    retval.append(str(i.clinic_phone))
                    retval.append(str(i.clinic_state))
                    retval.append(str(i.clinic_city))
                    retval.append(str(i.clinic_specialty))
                    retval.append(str(i.clinic_url))
            return retval
        elif field == "clinic_specialty" :
            for i in Clinic_list :
                if i.clinic_specialty == value :
                    retval.append(str(i.clinic_id))
                    retval.append(str(i.clinic_name))
                    retval.append(str(i.clinic_rating))
                    retval.append(str(i.clinic_phone))
                    retval.append(str(i.clinic_state))
                    retval.append(str(i.clinic_city))
                    retval.append(str(i.clinic_specialty))
                    retval.append(str(i.clinic_url))
            return retval
        elif field == "clinic_url" :
            for i in Clinic_list :
                if i.clinic_url == value :
                    retval.append(str(i.clinic_id))
                    retval.append(str(i.clinic_name))
                    retval.append(str(i.clinic_rating))
                    retval.append(str(i.clinic_phone))
                    retval.append(str(i.clinic_state))
                    retval.append(str(i.clinic_city))
                    retval.append(str(i.clinic_specialty))
                    retval.append(str(i.clinic_url))
            return retval
        else :
            "Error. Clinics does not have a propery " + str(field) + ".";

    def print_users(self) :
        for i in User_list :
            sys.stdout.write("user_id: " + str(i.user_id) + ", user_type: " + str(i.user_type) + " user_location: " + str(i.user_city) + ", " + str(i.user_state) +'\n')

    def print_clinics(self) :
        for i in Clinic_list :
            sys.stdout.write("clinic_id: " + str(i.clinic_id) + ", clinic_name: " + str(i.clinic_name) + ", clinic_rating: " + str(i.clinic_rating) + ", clinic_phone:" + str(i.clinic_phone) + ", clinic_state:" + str(i.clinic_state) + ", clinic_specialty:" + str(i.clinic_specialty) + ", clinic_URL: " + str(i.clinic_url)+ '\n')

    def print_questions(self) :
        for i in Question_list :
            sys.stdout.write("question_id:" + str(i.question_id) + ", question: " + str(i.question) + ", responses: ")
            for b in i.choices :
                sys.stdout.write(str(b) + " ")
            sys.stdout.write("\n")

    def print_links(self) :
        for i in Link_list :
            sys.stdout.write("link_id: " + str(i.link_id) + ", url: " + str(i.url) + ", user_type: " + str(i.user_type) + '\n')

def print_link(lst) :
    sys.stdout.write("link_id: " + str(lst[0]) + ", url: " + str(lst[1]) + ", user_type: " + str(lst[2]) + '\n')

def print_clinics(lst):
    sys.stdout.write("Clinic Name: " + lst.clinic_name + "\n")
    sys.stdout.write("Clinic Rating: " + lst.clinic_rating + "\n")
    sys.stdout.write("Clinic Phone: " + lst.clinic_phone + "\n")
    sys.stdout.write("Clinic Location: " + lst.clinic_city+ ", " + self.clinic_state + "\n")
    sys.stdout.write("Clinic Specialty: " + lst.clinic_specialty + "\n")
    sys.stdout.write("Clinic URL: " + lst.clinic_url + "\n")

def print_question(self) :
    sys.stdout.write("question_id:" + str(self.question_id) + ", question: " + str(self.question) + ", choices: ")
    for b in self.choices :
        sys.stdout.write(str(b) + " ")
    sys.stdout.write("\n")

def print_user(self) :
  	sys.stdout.write("user_id: " + str(user_id) + ", user_type: " + str(user_type) + ", user_location: " + str(user_city) + ", " + str(user_state) + '\n')

def populate_links(list_of_links) :
    list_of_links.append(Link(1, "hi.com", 1))
    list_of_links.append(Link(2, "ho.com", 1))
    list_of_links.append(Link(3, "he.com", 1))
    list_of_links.append(Link(4, "pi.com", 2))
    list_of_links.append(Link(5, "po.com", 2))
    list_of_links.append(Link(6, "pe.com", 2))
    list_of_links.append(Link(7, "ji.com", 3))
    list_of_links.append(Link(8, "jo.com", 3))
    list_of_links.append(Link(9, "je.com", 3))


def populate_clinics(list_of_clinics) :
    list_of_clinics.append(Clinic(1, "Clinic1", 1, "801-231-2312", "NY", "Marks", "Family Medicine", "thisclinic.com" ))
    list_of_clinics.append(Clinic(2, "Clinic2", 1, "801-231-2312", "TX", "Austin", "Internal Medicine", "thatclinic.com" ))
    list_of_clinics.append(Clinic(3, "Clinic3", 1, "801-231-2312", "VA", "Harmmony", "Rehab", "anotherclinic.com" ))
    list_of_clinics.append(Clinic(4, "Clinic4", 1, "801-231-2312", "NV", "Reno", "Luxury Rehab", "moreclinic.com" ))

def populate_questions(list_of_questions) :
    list_of_questions.append(Question(1, "What is your user type?", [1, 2, 3, 4]))
    list_of_questions.append(Question(2, "What is your state?", ["FREE-FORM"]))
    list_of_questions.append(Question(2, "What is your city?", ["FREE-FORM"]))

def populate_users(list_of_users) :
    list_of_users.append(User("struggling with addiction", 1, ["NY","Marks"]))
    list_of_users.append(User("at risk addiction", 2, ["TX","Austin"]))
    list_of_users.append(User("friend", 1, ["VA", "Harmony"]))
    list_of_users.append(User("family", 1, ["NV","Reno"]))

def populate_data_fields(links, questions, clinics, users) :
    populate_links(links)
    populate_clinics(clinics)
    populate_questions(questions)
    populate_users(users)
    return Database(links, questions, clinics, users);

#example "Create_ResponseList" call: Create_ResponseLisst(database.Quesiton_list, question_id)
#Create_ResponseList(database.Question_list, question_id)

def Create_ReponseList(myList, id):
    j = 1
    for val in myList:
        sys.stdout.write(j + ". " + str(myList(val)))
        for value in myList(val).choices :
            sys.stdout.write(str(myList(val).choices(value)))
    user_input = input()
    questionnaire[id].responses.append(user_input)
    j+=1

def evaluate_questionnaire(responses) :
      User(user_id, responses[0], responses [1], responses [2])




def run_tests () :
    print "Test 1: select_from_links test. Expected output: 1, \"hi.com\", 1"
    test1 = database.select_from_links("link_id", 1)
    print "Output >> ", ', '.join(test1), "\n"

    print "Test 2: select_from_links test. Expected output: 5, \"po.com\", 2"
    test2 = database.select_from_links("url", "po.com")
    print "Output >> ", ', '.join(test2), "\n"

    print "Test 3: select_from_links test. Expected output: 7, ji.com, 3, 8, jo.com, 3, 9, je.com, 3"
    test3 = database.select_from_links("user_type", 3)
    print "Output >> ", ', '.join(test3), "\n"


    print "Test 4: add new link to database \"1, to.com, 2\".... expected output as indicated in insert"
    database.insert_into_links(1, "to.com", 2)
    test4 = database.select_from_links("url", "to.com")
    print "Output >> ", ', '.join(test4), "\n"


Link_list = []
Clinic_list = []
Question_list = []
User_list = []
database = populate_data_fields(Link_list, Question_list, Clinic_list, User_list);

database.print_clinics()
database.print_questions()
database.print_links()
database.print_users()

#(Link) test1 = database.select_from_links("link_id", 1)

run_tests()
