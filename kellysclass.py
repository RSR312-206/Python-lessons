import math 

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def transpose (self, xdelta, ydelta):
        self.x = self.x + xdelta
        self.y = self.y + ydelta

    def status(self):
        print("point: %d, %d" % (self.x, self.y))
   
    def distance(self, other):
        a = other.y - self.y
        b = other.x - self.x
        rad = math.pow(a, 2) + math.pow(b, 2)
        return math.sqrt(rad)
#a^2 + b^2 = c^2

p = Point(5, 4)

p.status()

p.transpose(0,1) 

p.status()

p.transpose(1,1)

p.status()

p2 = Point(5, 1)

p3 = Point(6, 1)
 

print ("%f" % (p2.distance(p3)))

p4 = Point(2, 2)

p5 = Point(4, 4)

print ("%f" % (p4.distance(p5)))

p4.transpose(1, 2)

print ("%f" % (p5.distance(p4)))  

p6 = Point(-2, -2)

p7 = Point(-4, -4) 

print ("%f" %(p7.distance(p6)))

p8 = Point(2, -2)
p9 = Point(4, -4)

print ("%f" % (p9.distance(p8)))


p10 = Point(100, 100)









