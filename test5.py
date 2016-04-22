import sys
print "Running total : 0"
Next = float(raw_input("Next number: "))

def adder():
    Running_Total = 0
    print "Running total : " + str(float(Running_Total))
    Next = float(raw_input("Next number: "))
    adder(Running_Total + Next)

adder()
