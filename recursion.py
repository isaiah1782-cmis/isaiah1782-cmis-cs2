import sys
#Assignments: Countdown, Countup, Countdown from start to finish, Countup from finish to start

a = int(raw_input("Starting number: "))

b = int(raw_input("Ending number: "))

def countdown(start, stop):
    if start == stop or start >= stop:
        print 'Blastoff!'
    else:
        print start
        countdown(start+1, stop)

def countup(start, stop):
    if start == stop:
        print 'Blastoff!'
    else:
        print stop
        countup(start, stop-1)

print ""
print "Countup:"
print ""

countdown(a, b)

print ""
print "Countdown:"
print ""

countup(a, b)

#Assignments: Biggest, Smallest, pow(x, n), and Adder:
print ""
print "Finding the Biggest number:"
print ""

def biggest(biggest_number):
	number = raw_input("Next: ")
	if number == "":
		print "The biggest number is " + str(biggest_number) + "."
	elif float(number) > biggest_number:
		biggest(float(number))
	else:
		biggest(biggest_number)

biggest(-float("inf"))

print ""
print "Finding the Smallest number:"
print ""

def smallest(smallest_number):
    number = raw_input("Next: ")
    if number == "":
        print "The smallest number is " + str(smallest_number) + "."
    elif float(number) < smallest_number:
        smallest(float(number))
    else:
        smallest(smallest_number)

smallest(float("inf"))

print ""
print "Finding the Power"
print ""

x = raw_input("Number: ")
n = raw_input("Power: ")

def pow(x, n):
    if x == 0:
        return 0
    elif n == 0:
        return 1
    elif n == 0:
        return x
    elif n % 2 == 0:
        even = pow(x, n/2)
        return even * even
    else:
        n = (n-1)/2
        odd = pow(x, n)
        return x * odd * odd

print pow(float(x), float(n))

print ""
print "Finding the total:"
print ""

print "The running number is 0"

def adder(Number):
    Running_Total = 0
    Running_Total += Number
    Next = raw_input("Next number: ")
    if Next == "":
        sys.exit("The sum is " + str(Running_Total))
    else:
        Running_Total += int(Next)
        print "The running number is " + str(Running_Total)
        adder(Running_Total)

adder(0)
