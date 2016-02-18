import math
def add(x, y):
	return x + y
a1 = add(3, 4)
a2 = add(1, 6)
#I defined a function for each of the four basic math operations (+, -, *, /). I made each function took 2 arguments and returned the result.

def sub(x, y):
    return x - y
b1 = sub(3, 4)
b2 = sub(9, 10)
#I defined a function for each of the four basic math operations (+, -, *, /). I made each function took 2 arguments and returned the result.

def mul(x, y):
    return x * y
c1 = mul(4, 4)
c2 = mul(2, 8)
#I defined a function for each of the four basic math operations (+, -, *, /). I made each function took 2 arguments and returned the result.

def div(x, y):
    return x / y
d1 = div(2, 3)
d2 = div(21, 14.000000007)
#I defined a function for each of the four basic math operations (+, -, *, /). I made each function took 2 arguments and returned the result.

def hours_from_seconds(seconds):
    return seconds/3600
e1 = 1
e2 = 1
#I defined a function that took a number of seconds and returned the number of hours.

def circle_area(radius):
    return math.pi * (radius)**2
f1 = circle_area(5)**2
f2 = circle_area(100)**2
#I defined a function that took 1 argument that represented the radius of a circle. I made the function return the area of the circle.

def sphere_volume(radius):
    return 4/3 * math.pi * (radius)**3
g1 = sphere_volume(50)**3
g2 = sphere_volume(100)**3
#I defined a function that took 1 argument that represented the radius of a sphere and returned the volume.

def avg_volume(x, y):
    return ((4/3 * math.pi(x)**3)+(4/3 * math.pi(y)**3))/2

h1 = avg_volume(3, 4)**3
h2 = avg_volume(5, 20)**3
#I defined a function that took 2 integers that represented the diameters of a sphere. I made the function return the average of the volumes.

def area(x, y, z):
    p =(x+y+z)/2
    return (p*(p-x)*(p-y)*(p-z))**0.5
#I defined a function that took the 3 side lengths of a triangle as arguments and returned the area.

def right_align(word):
    return (80-len(word))*(" ") + word
#I defined a function that took a string as an argument and returned that word with additional spaces so that it was perfectly right aligned on the screen.

def center(word):
    return (40-len(word))*(" ") + word
#I defined a function that took a string as an argument and returned that word with additional spaces so that it was perfectly centered on the screen.

def msg_box(word):
    return "+" + ((len(word)+4)*"-")+"+"+"\n"+"|"+(2*"")+(word)+(2*"")+"|"+"\n"+"+"+((len(word)+4)*"-")+"+"
z1 = msg_box("Hello")
z2 = msg_box("I eat cats!")
