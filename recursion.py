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

#Biggest, smallest, and pow(x, n):
