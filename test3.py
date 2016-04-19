import string
import random
import time

print "Hi! This program will ask you to type some text and then It will try to guess it by random characters!"
print ""

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?/ ;:() *&^% $#@{} []`~ _=^-+"'

target = raw_input("Enter your text: ")
attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
attemptNext = ''

completed = False

generation = 0

while completed == False:
    print(attemptThis)
    attemptNext = ''
    completed = True
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += target[i]
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.1)

print("Target matched! The computer took " + str(generation) + " try(ies)!")
