import math
import random

Users_name = raw_input("Hello! What is your name?: ")
print ""
print "Hello " + str(Users_name) + "! Welcome to Isaiah's Text Game! Enjoy! :D"
print ""
print ""
print "Go to Google images and look up '32871'."
print ""
print ""
First_Random_Number = random.randint(1000, 9999)
Last_Random_Number = ((1782 + 31089) - (1782 + 18216)) - int(First_Random_Number)
Most_Important_Number = random.random()

print "So to start us off, I'm going to generate a random number."
print "Hmm.... I'll put down " + str(First_Random_Number) + "."

Users_Random_Four_Digit_Number = int(raw_input("""Now """ + str(Users_name) + """, please type a random four digit number (NO decimals/fractions/negatives and by saying "random" I want you to get creative): """))

print ""

def making_a_Random_Four_Digit_Number1():
    if Users_Random_Four_Digit_Number > 1000 and Users_Random_Four_Digit_Number < 10000 and Users_Random_Four_Digit_Number != 0000 and Users_Random_Four_Digit_Number != 1111 and Users_Random_Four_Digit_Number != 2222 and Users_Random_Four_Digit_Number != 3333 and Users_Random_Four_Digit_Number != 4444 and Users_Random_Four_Digit_Number != 5555 and Users_Random_Four_Digit_Number != 6666 and Users_Random_Four_Digit_Number != 7777 and Users_Random_Four_Digit_Number != 8888 and Users_Random_Four_Digit_Number != 9999:
        answer = 9999 - Users_Random_Four_Digit_Number
        print "Ok good! Now I'm going to generate another random number."
        print "The randomly generated number is " + str(answer) + "."
        Answer = random.randint(1000, 9999)
    elif Users_Random_Four_Digit_Number < 1000 or Users_Random_Four_Digit_Number > 10000:
        answer = 0
        print """Um """ + str(Users_name) + """, """ +  """ " """ + str(Users_Random_Four_Digit_Number) + """ " """ + """ is not a four digit number. An example of a four digit number is 1782 NOT 123 or 12345. Nice try though."""
        print ""
        print "Please redo the game again, " + str(Users_name) +  ".(Press the 'Enter' key twice)"
    elif Users_Random_Four_Digit_Number == 0000 or 1111 or 2222 or 3333 or 4444 or 5555 or 6666 or 7777 or 8888 or 9999:
        answer = 0
        print """Haha """ + str(Users_Random_Four_Digit_Number) + """ isn't a very creatively random 4 digit number."""
        print "Please redo the game again, " + str(Users_name) +  ".(Press the 'Enter' key twice)"
    return answer

x = making_a_Random_Four_Digit_Number1() #Programmer's Checkpoint

Users_Random_Four_Digit_Number2 = int(raw_input("""So now """ + str(Users_name) + """, please type another random four digit number (NO decimals/fractions/negatives and by saying "random" I want you to get creative): """))

def making_a_Random_Four_Digit_Number2():
    if Users_Random_Four_Digit_Number2 > 1000 and Users_Random_Four_Digit_Number2 < 10000 and Users_Random_Four_Digit_Number2 != 0000 and Users_Random_Four_Digit_Number2 != 1111 and Users_Random_Four_Digit_Number2 != 2222 and Users_Random_Four_Digit_Number2 != 3333 and Users_Random_Four_Digit_Number2 != 4444 and Users_Random_Four_Digit_Number2 != 5555 and Users_Random_Four_Digit_Number2 != 6666 and Users_Random_Four_Digit_Number2 != 7777 and Users_Random_Four_Digit_Number2 != 8888 and Users_Random_Four_Digit_Number2 != 9999:
        answer = 9999 - Users_Random_Four_Digit_Number2
        print "Ok good! Again, I'm going to generate another random number."
        print "The randomly generated number is " + str(answer) + "."
        Answer = random.randint(1000, 9999)
    elif Users_Random_Four_Digit_Number2 < 1000 or Users_Random_Four_Digit_Number2 > 10000:
        answer = 0
        print """Um """ + str(Users_name) + """, """ +  """ " """ + str(Users_Random_Four_Digit_Number2) + """ " """ + """ is not a four digit number. An example of a four digit number is 1782 NOT 123 or 12345. Nice try though."""
        print ""
        print "Please redo the game again, " + str(Users_name) +  ".(Press the 'Enter' key twice)"
    elif Users_Random_Four_Digit_Number2 == 0000 or 1111 or 2222 or 3333 or 4444 or 5555 or 6666 or 7777 or 8888 or 9999:
        answer = 0
        print """Haha """ + str(Users_Random_Four_Digit_Number2) + """ isn't a very creatively random 4 digit number."""
        print "Please redo the game again, " + str(Users_name) +  ".(Press the 'Enter' key twice)"
    return answer

y = making_a_Random_Four_Digit_Number2() #Programmer's Checkpoint

print ""
print "Ok! Now we're almost done. I am now going to generate the final random number."
print "I will say " + str(Last_Random_Number) + "!"
print ""

print "Yay! We are now done!"
print "Now... Time for the magic!"
print "You see, if we add all those numbers that we put down... what do we get?"
print ""
print "We get " + str(int(First_Random_Number) + int(Users_Random_Four_Digit_Number) + int(x) + int(Users_Random_Four_Digit_Number2) + int(y) + int(Last_Random_Number)) + "!"
print "Cool Eh?"
print ""
print ""
print ""
If_User_Thought_That_The_Text_Game_Was_Cool = raw_input("Did you like the game?(You can type 'Yes', 'No', or 'I didn't understand'): ")

def If_User_Thought_That_The_Text_Game_Was_Cool_Response():
    if str(If_User_Thought_That_The_Text_Game_Was_Cool) == "Yes" or str(If_User_Thought_That_The_Text_Game_Was_Cool) == "yes" or str(If_User_Thought_That_The_Text_Game_Was_Cool) == "YES":
        print "Great! My Job here is now done. Thanks for participating, " + str(Users_name) + ", and have a good day! :)"
        No = False
        x = bool(No)
    elif str(If_User_Thought_That_The_Text_Game_Was_Cool) == "No" or str(If_User_Thought_That_The_Text_Game_Was_Cool) == "no" or str(If_User_Thought_That_The_Text_Game_Was_Cool) == "NO":
        No = raw_input("Did you understand what was going on?(Yes or No): ")
        if No == Yes:
            print "Oh well. Have a good day and thanks for participating, " + str(Users_name) + "!"
    elif str(If_User_Thought_That_The_Text_Game_Was_Cool) == "I didn't understand" or str(If_User_Thought_That_The_Text_Game_Was_Cool) == "i didn't understand" or str(If_User_Thought_That_The_Text_Game_Was_Cool) == "i didnt understand" or str(If_User_Thought_That_The_Text_Game_Was_Cool) == "I don't get it" or str(If_User_Thought_That_The_Text_Game_Was_Cool) == "I dont get it" or str(If_User_Thought_That_The_Text_Game_Was_Cool) == "i dont get it" or str(If_User_Thought_That_The_Text_Game_Was_Cool) == "i don't get it":
        print ""
        print "Well what did I tell you to look up on Goole images?"
        No = True
        x = bool(No)
    return No

If_User_Thought_That_The_Text_Game_Was_Cool_Response()
