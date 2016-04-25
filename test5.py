def adder(Number):
    Running_Total = 0
    Running_Total += Number
    Next = raw_input("Next number: " + str(Running_Total) + """:
Next number: """
    if Next == "":
        exit("The sum is " + str(Running_Total))
    else:
        Total += int(Next)
        adder(Running_Total)

adder(0)
