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

countdown(a, b)
print ""
countup(a, b)

#Assignments: Biggest, Smallest, and pow(x, n):
print ""

def biggest(lastnumber):
	number = raw_input("Next: ")
	if number == '':
		print "The biggest number is " + str(lastnumber) + "."
	elif float(number) > lastnumber:
		biggest(float(number))
	else:
		biggest(lastnumber)

biggest(-float("inf"))

print ""



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
