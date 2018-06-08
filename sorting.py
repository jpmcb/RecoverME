
from math import sqrt

class Point: 
	def __init__ (self, x, y, name):
		self.x = x
		self.y = y
		self.name = name

def distance (myPoint, referencePoint):
		return sqrt((myPoint.x - referencePoint.x)**2 + (myPoint.y - referencePoint.y)**2)


clinicA = Point(1,2, "clinicA")
clinicB = Point(2,3, "clinicB")
clinicC = Point(27,49, "clinicC")
clinicD = Point(12,3, "clinicD")
clinicE = Point(14,-23, "clinicE")
clinicGPS = (clinicA, clinicB, clinicC, clinicD, clinicE)
myLocation= Point(40, -74, "myLocation")
print "Clinics Before Sort: "
for val in clinicGPS:
	print (val.name)
sortedGPS = sorted(clinicGPS, key=lambda p: distance(p, myLocation))
print "\n"
print "Clinics After Sort: "
for val in sortedGPS:
	print (val.name)

