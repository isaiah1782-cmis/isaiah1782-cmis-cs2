import math
import random

x = raw_input("What's your number guess?: ")

def guess(x):

	if x == 7:
		y = "You got that right!"
	elif x == 6:
		y = "You got that wrong!"
    else:
        y = random.randit(0,10)
    return y * random.random()


