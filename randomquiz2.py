print "Type 'Yes' for yes and 'No' for no"
def clapYourHands():
    print "Clap Clap"
def stompYourFeet():
    print "Stomp Stomp"
def main():
    youreHappy = raw_input("Are you happy?: ") == "Yes"
    youKnowIt = raw_input("Do you know that you are happy?: ") == "Yes"

    if youreHappy and youKnowIt:
        clapYourHands()
        stompYourFeet()

    print "Good bye"
main()
