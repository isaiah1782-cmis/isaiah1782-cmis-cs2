import sys
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
