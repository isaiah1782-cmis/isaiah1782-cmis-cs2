import time

#response collecting function
def response(prompt, allowed):
    resp = input(prompt)
    #check to see if response is in the set of allowed responses
    if resp in allowed:
        #return it if it is
        return resp
    else:
        #call response() again if it is not
        print('You have said soemthing that doesnt make sense! Your answer must be one of the following:\n' + ", ".join(allowed))
        return response(prompt, allowed)


#the list of questions
questions = [
    "0 + 0 = 0",
    "1 + 1 = 1",
    "1 * 1 == 2",
    "2 + 2 == 4",
    "2 * 2 == 4",
    "3 + 3 == 6",
    "3 * 3 == 9",
    "4 + 4 == 16",
    "4 * 4 == 16",
    "5 + 5 == 10",
    "5 * 5 == 25",
    "6 + 6 == 36",
    "6 * 6 == 12",
    "7 + 7 == 16",
    "7 * 7 == 14",
    "8 + 8 == 15",
    "8 * 8 == 16",
    "9 + 9 == 18",
    "9 * 9 == 81",
    "10 + 10 == 100",
    "10 * 10 == 100",
    "11 + 11 == 121",
    "11 * 11 == 221",
    "12 + 12 == 48",
    "12 * 12 == 144",
    ]

#score keeping variables
correct = 0
incorrect = 0

#Display some instructions and wait
print("Type 't' to answer for True.")
print("Type 'f' to answer for False.")
print("Hit the 'enter' or 'return' button to begin")

#start the timer
start = time.time()
print("The clock has now started! GO MY CHILD!!!")

#go through the list of questions
for q in questions:
    #display question and get answer
    answer = response(q + ": ", ['tz','f']) == 't'
    result = eval(q)
    #compare answer to actual result
    if answer == result:
        print("CONGRATULATIONS YOU GOT IT RIGHT! MOVE ON TO THE NEXT QUESTION!")
        correct += 1
    else:
        print("I'm sorry but what you said is wrong! Please try again!")
        incorrect += 1
    print(q + " is " + str(result) + "\n\n")
end = time.time()

#Display results
print("Wow! You took: ", end - start, " seconds to complete this random quiz!")
print("Congrats! You got ", correct, " question(s) correct! :D")
print("Sadly, you got ", incorrect, " question(s) incorrect.")
if incorrect > 0:
    print("I'm sorry but you have not passed! But DON'T CRY because you can just type 'python3 randomquiz.py' to retake the quiz again!")
else:
    print("FABULOS! 100%! YOU PASSED WITH FLYING COLOURS! CONRATS! :D Give yourself a pat on the back if you have arms. Type 'python3 randomquiz.py' to take the quiz again and beat your highscore!")
