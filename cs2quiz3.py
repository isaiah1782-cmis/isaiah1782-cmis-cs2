import sys
#Section 1: Terminology
# 1) What is a recursive function?
#
#A recursive function is a function that calls itself in the function so that it can keep on running.
#
# 2) What happens if there is no base case defined in a recursive function?
#
#If there isn't a base case defined in a recursive function then it will call itslef infinity times.
#
# 3) What is the first thing to consider when designing a recursive function?
#
#How it stops.
#
# 4) How do we put data into a function call?
#
#We can use raw_input or when we call it again we add an equation inside the brackets so that when it is called again then it will add the equation.
# 
# 5) How do we get data out of a function call?
#
#We can use the return command so that when we call the function it will return the data.
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 
#b2 = 
#b3 = 

#c1 = 
#c2 = 
#c3 = 

#d1 = 6
#d2 = 
#d3 = 

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


def main(total, division):
    #base case
    Next = raw_input("Next: ")
    if Next == "":
        print "The average of your odd numbers was " + str(float(float(total)/float(division))) + "."
        sys.exit()
    #recursive case
    if int(Next) % 2 == 0:
        division += 0
        total += 0
        main(total, division)
    #recursive case
    else:
        division += 1
        total += int(Next)
        main(total, division)

main(0, 0)



















