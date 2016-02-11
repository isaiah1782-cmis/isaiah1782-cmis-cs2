def add(x, y):
	return x + y
#I defined a function for each of the four basic math operations (+, -, *, /). I made each function took 2 arguments and returned the result.

def sub(x, y):
    return x - y
#I defined a function for each of the four basic math operations (+, -, *, /). I made each function took 2 arguments and returned the result.

def mul(x, y):
    return x * y
#I defined a function for each of the four basic math operations (+, -, *, /). I made each function took 2 arguments and returned the result.

def div(x, y):
    return x / y
#I defined a function for each of the four basic math operations (+, -, *, /). I made each function took 2 arguments and returned the result.

def hours_from_seconds(seconds):
    return seconds/3600
#I defined a function that took a number of seconds and returned the number of hours.

def circle_area(radius):
    return math.pi(radius)**2
#I defined a function that took 1 argument that represented the radius of a circle. I made the function return the area of the circle.

def sphere_volume(radius):
    return 4/3 * math.pi(radius)**3
#I defined a function that took 1 argument that represented the radius of a sphere and returned the volume.

def avg_volume(x, y):
    return ((4/3 * math.pi(x)**3)+(4/3 * math.pi(y)**3))/2
#I defined a function that took 2 integers that represented the diameters of a sphere. I made the function return the average of the volumes.

def area(x, y, z):
    p =(x+y+z)/1
    return math.sqrt(p*(p-x)(p-y)(p-z))
#I defined a function that took the 3 side lengths of a triangle as arguments and returned the area.

def right_align(abc):
    len(abc) 
#I defined a function that took a string as an argument and returned that word with additional spaces so that it was perfectly right aligned on the screen.
