import math
import random

Minimum_Number = int(raw_input("What is the minimum number? "))
Maximum_Number = int(raw_input("What is the maximum number? "))

def Finding_a_Number():
    number = random.randint(Minimum_Number, Maximum_Number)
    return number

print "I'm thinking of a number from " + str(Minimum_Number) + " to " + str(Maximum_Number) + "."

Guess = str(raw_input("What do you think it is?: "))

print ""
print "The target was " + str(Finding_a_Number()) + "."
print "Your guess was " + str(Guess) + "."

def Did_You_Guess_it_Correctly():
    if Guess == str(Finding_a_Number()):
        y = True
    return y

def You_Guessed_it():
    if Did_You_Guess_it_Correctly() == True:
        a = "Congrats!"
    return a

def Under_or_Over():
    if str(Finding_a_Number()) > Guess:
        return True
    elif str(Finding_a_Number()) < Guess:
        return False

def Is_Under_or_Over_True_or_False():
    if Under_or_Over() == True:
        x = "That's over by "
    if Under_or_Over() == False:
        x = "That's under by "
    return x

print Is_Under_or_Over_True_or_False()
