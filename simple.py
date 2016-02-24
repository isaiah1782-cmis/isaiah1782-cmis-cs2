import math

print "Area of a Triangle calculator:"
print ""

def area(x, y, z):
    p = (x+y+z)/2
    return (p*(p-x)*(p-y)*(p-z))**0.5

l = raw_input("What's the length?: ")
w = raw_input("What's the width?: ")
h = raw_input("What's the hieght?: ")
units = raw_input("What's the measurement?(If you don't know then just say 'Units'): ")

a = area(int(l), int(w), int(h))

print "The area of your triangle is " + str(a) + str(units) + "³."
