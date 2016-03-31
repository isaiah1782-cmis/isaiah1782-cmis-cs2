#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a)
#   >>>bool(1)
#   >>>True
#b)
#   >>>bool(0)
#   >>>False
#c)
#   >>>p = False
#   >>>bool(p)
#   >>>False
#
#2) What does 'return' do?
#
#The retrun command puts a variable's assigned value, that you assigned in a function, for the function so that you can call the function's value in a variable without running the function again.
#
#3) What are 2 ways indentation is important in python code?
#
#Indentation is important in python code because:
#a)It can tell whenever something is a part of something, like a function.
#b)It can seperate two different things that wern't meant to be together.
#
#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) -36
#problem1_b) -9
#problem1_c) square root of 0 times negative 1 (0)
#problem1_d) -(abs(-5))
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) False
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 
#problem4_d) 
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

import math

print "Type in 3 different numbers (decimals are OK!)"

a = float(raw_input("A: "))
b = float(raw_input("B: "))
c = float(raw_input("C: "))

def if_numbers_were_the_same():
    if a == b and a == c or a == c or a == b:
        exit("You didn't follow directions")
    elif b == a and b == c or b == a or b == c:
        exit("You didn't follow directions")
    elif c == a and c == b or c == a or c == b:
        exit("You didn't follow directions")

def main():
    if a > b and a > c:
        output = "The largest number was " + str(a) 
    elif b > a and b > c:
        output = "The largest number was " + str(b)
    elif c > a and c > b:
        output = "The largest number was " + str(c)
    return output

if_numbers_were_the_same()

x = main()

print x
