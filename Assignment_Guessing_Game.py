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

def Correct_or_Over_or_under
    if target == your_number: 
		print """
Your target was {}.
Your guess was {}.
That's correct! You must be psychic!
		""".format(target, your_number)
	elif target > your_number:
		sub = target - your_number
		print """
Your target was {}.
Your guess was {}.
That's under by {}.
		""".format(target, your_number, sub)
	elif target < your_number:
		sub = your_number - target 
		print """
Your target was {}.
Your guess was {}.
That's over by {}.
		""".format(target, your_number, sub)
