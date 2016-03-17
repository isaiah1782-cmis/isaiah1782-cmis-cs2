import math
import random

Minimum_Number = int(raw_input("What is the minimum number? "))
Maximum_Number = int(raw_input("What is the maximum number? "))

print "I'm thinking of a number from " + str(Minimum_Number) + " to " + str(Maximum_Number) + "."

Guess = str(raw_input("What do you think it is?: ")) 

def Correct_or_Over_or_under():
    x = number = random.randint(Minimum_Number, Maximum_Number)
    if int(x) == int(Guess):
        print """
The target was {}.
Your guess was {}.
That's correct! You must be psychic!
		""".format(str(x), str(Guess))
    elif str(x) > str(Guess):
        Under = int(x) - int(Guess)
        print """
The target was {}.
Your guess was {}.
That's under by {}.
		""".format(str(x), str(Guess), Under)
    elif str(x) < str(Guess):
        Over = int(Guess) - int(x)
        print """
The target was {}.
Your guess was {}.
That's over by {}.
		""".format(str(x), str(Guess), Over)

Correct_or_Over_or_under()
