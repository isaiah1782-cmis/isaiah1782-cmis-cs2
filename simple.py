x = raw_input("Type you favouite number: ")
y = raw_input("Type a random number: ")
z = int(x) + int(y)
print str(x) + "+" + str(y) + "=" + str(z)
print " "
print " "
print " "
a = raw_input("What is 19 - 10: ")
b = raw_input("What is 19 - 9: ")
c = int(a) + int(b)
print str(a) + " + " + str(b) + " = 21"
print "No, you stupid"
print " "
print " "
print " "
d = raw_input("What is the first letter of your name: ")
e = raw_input("What is the first letter of your middle name: ")
f = raw_input("What is the first letter of your last name: ")
print "Your initials are: " + str(d) + "." + str(e) + "." + str(f) + "."

print " "

name = raw_input("What's your name?: ")

output = """
Hey {}!
Did you know that:
{} + {} = {}
And
{} - {} = {}
""".format(name, x, y, z, z, y, x)

print output

print " "
print " "
print " "

Prince_or_Princess = raw_input("Would you rather be a Prince or Princess?: ")
He_or_She = raw_input("Would you rather be called He or She?: ")
His_or_Her = raw_input("Would you rather be called His or Her? ")
Home = raw_input("What kind of house would you like to live in?: ")
Planet = raw_input("What planet would you like to live on?: ")

print

print "There once was a brilliant " + str(Prince_or_Princess) + " named " + str(name) + ". " + str(He_or_She) + " lived in a " + str(Home) + " on " + str(Planet) + ". " + str(name) + " loved the number " + str(x) + ". " + "In " + str(His_or_Her) + " " + str(Home) + ", " + str(name) + " liked to do "
