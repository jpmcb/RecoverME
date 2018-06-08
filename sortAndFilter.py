from math import sqrt
import unittest
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
        for j in i.keywords :
            if j in keywords :
                filtered.append(i)
    return filtered

#userType cannot be null else there's nothing to sort on. Keywords can be null.
#If keywords not supplied then all links taylored to this user type is returned.
#If keywords are supplied then links taylored to the user and their preferences
#are returned.
def refineUserLinks(links, userType, keywords = "NULL") :
    unrefinedLinks = filterByUserType(links, userType)
    if keywords == "NULL" :
        return unrefinedLinks
    else :
        return filterByKeywords(links, keywords)

#clinic
#Parameters: location = 2 element list with x in position 0 and y in position 1,
#				facility_type is the kind of facitiy and should be of type string,
#				name is the name of the facility.
#Member variables: facility_type same as parameter, name same as parameter,
#				location is a point object created using location list parameter.
class Clinic :
    def __init__(self, name, location, facility_type) :
        self.location = point(location[0], location[1], name)
        self.name = name
        self.facility_type - facility_type

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
    sortedGPS = sorted(clinicGPS, key=lambda p: distance(p, curLocation)) #sort function!
    return sortedGPS

clinicA = Point(1,2, "clinicA")
clinicB = Point(2,3, "clinicB")
clinicC = Point(27,49, "clinicC")
clinicD = Point(12,3, "clinicD")
clinicE = Point(14,-23, "clinicE")
clinicGPS = (clinicA, clinicB, clinicC, clinicD, clinicE)
myLocation= Point(40, -74, "myLocation")
print "Clinics Before Distance Sort: "
for val in clinicGPS:
    print ("Name: ", val.name)
print "\n"
print "Clinics After Distance Sort: "
for val in sortByDistance(clinicGPS, myLocation):
    print (val.name)



class TestPoints(unittest.TestCase):
    def test_distance(self):
    # test negatives
        clinicA = Point(-10, -15, "clinicA")
        clinicB = Point(0, 0, "clinicB")
        a_to_b = distance(clinicA, clinicB)
        self.assertEqual(a_to_b, 25)
    # test same point
        clinicC = Point(10, 25, "clinicC")
        clinicD = Point(10, 25, "clinicD")
        c_to_d = distance(clinicC, clinicD)
        self.assertEqual(c_to_d, 0)
    # test positives
        clinicE = Point(20, 15, "clinicE")
        clinicF = Point(5, 10, "clinicF")
        e_to_f = distance(clinicE, clinicF)
        self.assertEqual(e_to_f, 20)

    def test_sortByDistance(self):
        clinicA = Point(1,2, "clinicA")
        clinicB = Point(2,3, "clinicB")
        clinicC = Point(27,49, "clinicC")
        clinicD = Point(12,3, "clinicD")
        clinicE = Point(14,-23, "clinicE")
        clinicGPS = (clinicA, clinicB, clinicC, clinicD, clinicE)
        myLocation= Point(40, -74, "myLocation")
        sorted_clinics = sortByDistance(clinicGPS, mylocation)

        for i in range(0, len(sorted_clinics) - 1):
            self.assertTrue(distance(myLocation, sorted_clinics[i]) <= distance(myLocation, sorted_clinics[i + 1]))

class TestFilters(unittest.TestCase):
    def test_filterByKeyword():
        testlink1 = Link("www.testurl.com", "friend", ["keyword1"])
        testlink2 = Link("www.testurl2.com", "addict", ["keyword1"])
        testlink3 = Link("www.testurl3.com", "suspected addict", ["keyword1"])
        testlink4 = Link("www.testurl3.com", "friend", ["keyword2"])
        testlink5 = Link("www.testurl3.com", "addict", ["keyword1","keyword3"])
        testlink6 = Link("www.testurl3.com", "suspected addict", ["keyword4"])
        links = [testlink1, testlink2, testlink3, testlink4, testlink5, testlink6]
        filtered = filterByKeywords(links, "keyword1")
        for link in filtered:
            self.assertTrue(link.key_words == "keyword1")

    def test_filterByUserType():
        print "testing links"
        testlink1 = Link("www.testurl.com", "friend", "keyword1")
        testlink2 = Link("www.testurl2.com", "addict", "keyword1")
        testlink3 = Link("www.testurl3.com", "suspected addict", "keyword1")
        testlink4 = Link("www.testurl3.com", "friend", "keyword2")
        testlink5 = Link("www.testurl3.com", "addict", "keyword3")
        testlink6 = Link("www.testurl3.com", "suspected addict", "keyword4")
        links = [testlink1, testlink2, testlink3, testlink4, testlink5, testlink6]
        filtered = filterByUserType(links, "friend")

        for link in filtered:
            self.assertEqual(link.user_type, "friend")

    def test_filterByFacilityType():
        location1 = [1, 2]
        location2 = [3, 4]
        location3 = [4, 5]
        testfacility1 = Clinic("facilityX", location1, "rehab")
        testfacility2 = Clinic("facilityY", location2, "medical")
        testfacility3 = Clinic("facilityZ", location3, "support group")
        facilities = [testfacility1, testfacility2, testfacility3]
        filtered = filterByFacilityType(facilities, "rehab")

        for facility in filtered:
            self.assertEqual(link.facility_type, "rehab")
