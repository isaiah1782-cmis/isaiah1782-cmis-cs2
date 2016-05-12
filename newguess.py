import random

print "You have 3 rounds to guess 3 numbers between 0 and 100. The program will tell you if you're you guess is higher than the number and if you're guess is lower than the number. You have 10 tries for each round"

def main(Number_of_Tries, The_Number):
    Users_Guess = int(raw_input("What's your guess?: "))
    if Number_of_Tries == 0:
        print "You have run out of tries! You are still awesome though."
    elif Users_Guess == The_Number:
        print "Congratulations! You have guessed the number!"
    elif Users_Guess > The_Number:
        print "Thats too high"
        main(Number_of_Tries - 1, The_Number)
    elif Users_Guess < The_Number:
        print "Thats too low"
        main(Number_of_Tries - 1, The_Number)

import time
start_time = time.time()

print ""
print "Round 1"
print ""
main(10, random.randint(0, 100))

print ""
print "Round 2"
print ""
main(10, random.randint(0, 100))

print ""
print "Round 3"
print ""
main(10, random.randint(0, 100))



print("You took %s seconds to finish!" % (time.time() - start_time))
