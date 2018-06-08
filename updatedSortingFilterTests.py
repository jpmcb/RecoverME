
import unittest
from sortingAndFilter import Point, Link, Clinic, distance, sortByDistance
from sortingAndFilter import filterByKeywords, filterByFacility, filterByUserType

class TestPoints(unittest.TestCase):
    def test_distance(self):
        # test negatives
        clinicA = Point(-10, -15, "clinicA")
        clinicB = Point(0, 0, "clinicB")
        a_to_b = distance(clinicA, clinicB)
        self.assertTrue(a_to_b - 18.0277563 < 0.1)
        # test same point
        clinicC = Point(10, 25, "clinicC")
        clinicD = Point(10, 25, "clinicD")
        c_to_d = distance(clinicC, clinicD)
        self.assertEqual(c_to_d, 0)
        # test positives
        clinicE = Point(20, 15, "clinicE")
        clinicF = Point(5, 10, "clinicF")
        e_to_f = distance(clinicE, clinicF)

        self.assertTrue(e_to_f - 15.81138830084196 < 0.1)

    def test_sortByDistance(self):
        clinicA = Point(1,2, "clinicA")
        clinicB = Point(2,3, "clinicB")
        clinicC = Point(27,49, "clinicC")
        clinicD = Point(12,3, "clinicD")
        clinicE = Point(14,-23, "clinicE")
        clinicGPS = (clinicA, clinicB, clinicC, clinicD, clinicE)
        myLocation= Point(40, -74, "myLocation")
        sorted_clinics = sortByDistance(clinicGPS, myLocation)
        for i in range(0, len(sorted_clinics) - 1):
            self.assertTrue(distance(myLocation, sorted_clinics[i]) <= distance(myLocation, sorted_clinics[i + 1]))

class TestFilters(unittest.TestCase):
    def test_filterByKeyword(self):
        testlink1 = Link("www.testurl.com", "friend", ["keyword1"])
        testlink2 = Link("www.testurl2.com", "addict", ["keyword1"])
        testlink3 = Link("www.testurl3.com", "suspected addict", ["keyword1"])
        testlink4 = Link("www.testurl4.com", "friend", ["keyword2", "keyword1"])
        testlink5 = Link("www.testurl5.com", "addict", ["keyword3"])
        testlink6 = Link("www.testurl6.com", "suspected addict", ["keyword4"])
        links = [testlink1, testlink2, testlink3, testlink4, testlink5, testlink6]
        filtered = filterByKeywords(links, ["keyword1"])
        for link in filtered:
            self.assertTrue("keyword1" in link.key_words)

    def test_filterByUserType(self):
        testlink1 = Link("www.testurl.com", "friend", ["keyword1"])
        testlink2 = Link("www.testurl2.com", "addict", ["keyword1"])
        testlink3 = Link("www.testurl4.com", "suspected addict", ["keyword1"])
        testlink4 = Link("www.testurl5.com", "friend", ["keyword2"])
        testlink5 = Link("www.testurl6.com", "addict", ["keyword3"])
        testlink6 = Link("www.testurl7.com", "suspected addict", ["keyword4"])
        links = [testlink1, testlink2, testlink3, testlink4, testlink5, testlink6]
        filtered = filterByUserType(links, "friend")
        for link in filtered:
            self.assertEqual(link.user_type, "friend")

    def test_filterByFacility(self):
        location1 = [1, 2]
        location2 = [3, 4]
        location3 = [4, 5]
        testfacility1 = Clinic("facilityX", location1, "rehab")
        testfacility2 = Clinic("facilityY", location2, "medical")
        testfacility3 = Clinic("facilityZ", location3, "support group")
        facilities = [testfacility1, testfacility2, testfacility3]
        filtered = filterByFacility(facilities, "rehab")
        for i in range(0, len(filtered)):
            self.assertEqual(filtered[i][0], "rehab")

if __name__ == '__main__':
    unittest.main()
