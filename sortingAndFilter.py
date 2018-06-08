from math import sqrt
import operator

class Point:
    def __init__ (self, x, y, name):
        self.x = x
        self.y = y
        self.name = name


#link class - url = URL of link, user_typ = list of user types this link is for,
#key_words = relevant link keywords
class Link :
    def __init__(self, url, user_type, key_words) :
        self.url = url
        self.user_type = user_type
        self.key_words = key_words

#filter a list of links on the user type (string)
def filterByUserType(links, type) :
    filtered = []
    for i in links :
        if type in i.user_type :
            filtered.append(i)
    return filtered

#quick and dirty filter by keywords
def filterByKeywords(links, keywords) :
    filtered = []
    for i in links :
        for j in i.key_words :
            if j in keywords :
                filtered.append(i)
                break
    return filtered

#userType cannot be null else there's nothing to sort on. Keywords can be null.
#If keywords not supplied then all links taylored to this user type is returned.
#If keywords are supplied then links taylored to the user and their preferences
#are returned.
def refineUserLinks(links, userType, keywords = "NULL") :
    unrefinedLinks = filterByUserType(links, userType)
    if keywords == "NULL" :
        return unrefinedLinks
    else:
        return filterByKeywords(unrefinedLinks, keywords)

#clinic
#Parameters: location = 2 element list with x in position 0 and y in position 1,
#				facility_type is the kind of facitiy and should be of type string,
#				name is the name of the facility.
#Member variables: facility_type same as parameter, name same as parameter,
#				location is a point object created using location list parameter.
class Clinic :
    def __init__(self, name, location, facility_type) :
        self.location = Point(location[0], location[1], name)
        self.name = name
        self.facility_type = facility_type

#filter facilitys according to their primary mode of service
def filterByFacility(clinics, keywords) :
    filteredList = {}
    for i in clinics :
        if i.facility_type in keywords :
            filteredList[i.facility_type] = i

    sortedTuple = sorted(filteredList.items(), key=operator.itemgetter(1))
    return sortedTuple

def distance (myPoint, referencePoint):
    return sqrt((myPoint.x - referencePoint.x)**2 + (myPoint.y - referencePoint.y)**2)

def sortByDistance(clinics, curLocation):
    sortedGPS = sorted(clinics, key=lambda p: distance(p, curLocation)) #sort function!
    return sortedGPS
