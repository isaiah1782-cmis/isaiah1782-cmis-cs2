print '\033[1;37mHello and welcome to my \033[1;m' + "" + '\033[1;31mC\033[1;m' + '\033[1;33mo\033[1;m' + '\033[1;32ml\033[1;m' + '\033[1;36mo\033[1;m' + '\033[1;34mu\033[1;m' + '\033[1;35mr\033[1;m' + " " + '\033[1;37mPrinter!\033[1;m'
print ""
print "Colours of Text:"
print '\033[1;31mRed\033[1;m'
print '\033[1;33mYellow\033[1;m'
print '\033[1;32mGreen\033[1;m'
print '\033[1;36mCyan\033[1;m'
print '\033[1;34mBlue\033[1;m'
print '\033[1;35mPurple\033[1;m'
print '\033[1;30mGray\033[1;m'
print '\033[1;37mWhite\033[1;m'
print ""
print "Colours of Highlight:"
print '\033[1;41mRed\033[1;m'
print '\033[1;43mYellow\033[1;m'
print '\033[1;42mGreen\033[1;m'
print '\033[1;46mCyan\033[1;m'
print '\033[1;44mBlue\033[1;m'
print '\033[1;45mPurple\033[1;m'
print '\033[1;47mGray\033[1;m'
print ""

def Colour_Maker():
    output = 0
    output2 = 0
    Colour = raw_input("Colour: ")
    if Colour == "":
        pass
    print ""
    if Colour == "Red" or Colour == "red":
        output += 31
    if Colour == "Yellow" or Colour == "yellow":
        output += 33
    if Colour == "Green" or Colour == "green":
        output += 32
    if Colour == "Cyan" or Colour == "cyan":
        output += 36
    if Colour == "Blue" or Colour == "blue":
        output += 34
    if Colour == "Purple" or Colour == "purple":
        output += 35
    if Colour == "Gray" or Colour == "gray":
        output += 30
    if Colour == "White" or Colour == "white":
        output += 37
    Highlight = raw_input("Highlight: ")
    if Highlight == "":
        pass
    if Highlight == "Red" or Highlight == "red":
        output2 += 41
    if Highlight == "Yellow" or Highlight == "yellow":
        output2 += 43
    if Highlight == "Green" or Highlight == "green":
        output2 += 42
    if Highlight == "Cyan" or Highlight == "cyan":
        output2 += 46
    if Highlight == "Blue" or Highlight == "blue":
        output2 += 44
    if Highlight == "Purple" or Highlight == "purple":
        output2 += 45
    if Highlight == "Gray" or Highlight == "gray":
        output2 += 47
    print ""
    Text = raw_input("Text: ")
    if output == 0 and output2 == 0:
        pass
    if output != 0 and output2 == 0:
        print ""
        print '\033[1;{0}m{1}\033[1;m'.format(output2, Text)
        print ""
    if output == 0 and output2 != 0:
        print ""
        print '\033[1;{0}m{1}\033[1;m'.format(output, Text)
        print ""
    else:
        print ""
        print '\033[1;{0}m\033[1;{1}m{2}\033[1;m\033[1;m'.format(output2, output, Text)
        print ""
        Colour_Maker()
Colour_Maker()
