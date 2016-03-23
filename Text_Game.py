import math
import random

Users_name = raw_input("Hello! What is your name?: ")
print ""
print "Hello " + str(Users_name) + "! Welcome to Isaiah's Text Game! Enjoy! :D"
print ""

Users_Random_Four_Digit_Number = int(raw_input("""So """ + str(Users_name) + """, to start off, please type a random four digit number (NO decimals/fractions/negatives and by saying "random" I want you to get creative): """))

print ""

def making_a_Random_Four_Digit_Number1():
    if Users_Random_Four_Digit_Number > 1000 and Users_Random_Four_Digit_Number < 9999:
        answer = 9999 - Users_Random_Four_Digit_Number
        print "Ok so now I'm going to add my random number to your random number number."
        print "I'll say " + str(answer) + "."
    elif Users_Random_Four_Digit_Number < 1000:
        answer = 0
        print """Um """ + str(Users_name) + """, """ +  """ " """ + str(Users_Random_Four_Digit_Number) + """ " """ + """ is not a four digit number. An example of a four digit number is 1782 NOT 123 or 12345. Nice try though."""
        print ""
        print "Please redo the game again, " + str(Users_name) +  "."
    elif Users_Random_Four_Digit_Number > 1000:
        answer = 0
        print """Um """ + str(Users_name) + """, """ + """ " """ + str(Users_Random_Four_Digit_Number) + """ " """ + """ is not a four digit number. An example of a four digit number is 1782 NOT 123 or 12345. Nice try though."""
        print ""
        print "Please redo the game again, silly."
    if Users_Random_Four_Digit_Number == 0000 or 1111 or 2222 or 3333 or 4444 or 5555 or 6666 or 7777 or 8888 or 9999:
        answer = 0
        print """Haha """ + """ isn't a very creatively random 4 digit number """
        print "Please redo the game again, " + str(Users_name) +  "."
    return answer

x = making_a_Random_Four_Digit_Number1()





