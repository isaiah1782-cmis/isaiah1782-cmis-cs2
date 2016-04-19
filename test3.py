import string
import random
import time

print "Hi! This program will ask you to type some text and then it will try to guess your text by random characters!"
print ""

a = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?/ ;:() *&^% $#@{} []`~ _=^-+"'

target = raw_input("Enter your text: ")
b = ''.join(random.choice(a) for i in range(len(target)))
c = ''

completed = False

generation = 0

while completed == False:
    print(b)
    c = ''
    completed = True
    for i in range(len(target)):
        if b[i] != target[i]:
            completed = False
            c += random.choice(a)
        else:
            c += target[i]
    generation += 1
    b = c
    time.sleep(0.1)

print("Target matched! The computer took " + str(generation) + " try(ies)!")
