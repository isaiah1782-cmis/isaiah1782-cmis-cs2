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
e2 = 2
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
    h1 = x/2
    h2 = y/2
    x = 4/3*math.pi*h1*h1*h1
    z = 4/3*math.pi*h2*h2*h2
    return (y+z)/2
h3 = avg_volume(9, 10)
h4 = avg_volume(50, 100)
#I defined a function that took 2 integers that represented the diameters of a sphere. I made the function return the average of the volumes.

def area(x, y, z):
    p =(x+y+z)/2
    return (p*(p-x)*(p-y)*(p-z))**0.5
i1 = area(1, 2, 2.5)
i2 = area(10, 20, 25)
#I defined a function that took the 3 side lengths of a triangle as arguments and returned the area.

def right_align(word):
    return (80-len(word))*(" ") + word
j1 = right_align("Hello")
j2 = right_align("Its me")
#I defined a function that took a string as an argument and returned that word with additional spaces so that it was perfectly right aligned on the screen.

def center(word):
    return (40-len(word))*(" ") + word
k1 = center("Hi")
k2 = center("Eat Frogs!")
#I defined a function that took a string as an argument and returned that word with additional spaces so that it was perfectly centered on the screen.

def msg_box(word):
    return "+" + ((len(word)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word)+4)*"-") + "+"
l1 = msg_box("Hello")
l2 = msg_box("I eat cats!")
# I defined a function that took a string as an argument and returned the message box like below:
#+---------+
#|  Hello  |
#+---------+
#+---------------+
#|  I eat cats!  |
#+---------------+

print msg_box(str(a1))
print msg_box(str(a2))
print msg_box(str(b1))
print msg_box(str(b2))
print msg_box(str(c1))
print msg_box(str(c2))
print msg_box(str(e1))
print msg_box(str(e2))
print msg_box(str(f1))
print msg_box(str(f2))
print msg_box(str(g1))
print msg_box(str(g2))
print msg_box(str(h3))
print msg_box(str(h4))
print msg_box(str(i1))
print msg_box(str(i2))
print msg_box(str(j1))
print msg_box(str(j2))
print msg_box(str(k1))
print msg_box(str(k2))
print l1
print l2
