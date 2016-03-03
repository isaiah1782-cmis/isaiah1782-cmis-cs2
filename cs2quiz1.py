#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#
# "=" Is the assignment operator/statement and it creates new variables and gives them values.
#
#2 3pts) Write a technical definition for 'function'
#
# In the context of programming, a function is a named sequence of statements that performs a computation. When you define a function, you specify the name and the sequence of statements.
#
#3 1pt) What does the keyword "return" do?
#
# The "return" keyword The expression in parentheses is called the argument of the function. The result, for this function, is the type of the argument.
# It is common to say that a function takes an argument and returns a result. The result is called the return value. This statement means: Return immediately from this function and use the 
# following expression as a return value.
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: or ( 1>2 or 2>1) (454>123 or 123>454)
#	2: and (1 == 1 and 2 == 2) (21 > 9 and 10 < 21)
#	3: not (3>2 not 2>3) (54>1 not 1>54)
#	4: is (1 is 1.0) (5 is 5.0)
#	5: if (True == False if False == True) (1>2 if 2<1)
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#
# A "function definition" is defining the function and a "function call" is calling the function using numbers or variables. 
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them?
#	1: int() : This takes the string/number and truns it into an integer so that you can use it to do math problems.
#	2: str() : This takes anything and puts it into a string so that you can print out a sentence with numbers.
#	3: float() :This takes any number/integer and turns it into a decimal.
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math

C1 = raw_input("Area of C1: ")
C2 = raw_input("Area of C2: ")
C3 = raw_input("Area of C3: ")

def circle_diameter(area):
    return math.sqrt(((area) / math.pi)) + math.sqrt(((area) / math.pi))

print ""

CD1 = math.sqrt(((float(C1)) / math.pi)) + math.sqrt(((float(C1)) / math.pi))
CD2 = math.sqrt(((float(C2)) / math.pi)) + math.sqrt(((float(C2)) / math.pi))
CD3 = math.sqrt(((float(C3)) / math.pi)) + math.sqrt(((float(C3)) / math.pi))

Total = float(CD1) + float(CD2) + float(CD3)

print "Circle  Diameter"
print "c1      " + str(CD1)
print "c2      " + str(CD2)
print "c3      " + str(CD3)
print "Totals  " + str(Total)
