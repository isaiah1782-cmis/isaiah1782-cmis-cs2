import math

print "Area of a Triangle calculator:"
print ""

def area(width, height):
    area = (width * height) * 0.5
    return area

def sphere_volume(radius):
    return 4/3 * (math.pi * (radius))

def main():
    w = raw_input("What's the base?: ")
    h = raw_input("What's the hieght?: ")
    units = raw_input("What's the measurement?(If you don't know then just say 'Units'): ")
    area_of_Triange = area(int(w), int(h))
    print ""
    print "The area of your triangle is {}".format(int(area_of_Triange)) + str(units) + "."
    print ""
    print "Volume of a Sphere calcualtor:"
    print ""
    radius = raw_input("What's the radius?: ")
    units1 = raw_input("What's the measurement?(If you don't know then just say 'Units'): ")
    volume_of_Sphere = sphere_volume(int(radius))
    print ""
    print "The volume of your sphere is {}".format(int(volume_of_Sphere)) + str(units) + "."

main()
