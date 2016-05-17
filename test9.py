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
    Colour = raw_input("Colour: ")
    if Colour == "":
        pass
    print ""
    if Colour == "Red":
        output += 31
    if Colour == "Yellow":
        output += 33
    Highlight = raw_input("Highlight: ")
    if Highlight == "":
        output2 = 0
        pass
    Text = raw_input("Text: ")
    if output2 == 0:
        print '\033[1;{0}m{0}\033[1;m'.format(output, Text)
Colour_Maker()


y = 31
print '\033[1;{0}mRed\033[1;m'.format(y)



print ""
print '\033[1;30mGray like Ghost\033[1;m'
print '\033[1;31mRed like Radish\033[1;m'
print '\033[1;32mGreen like Grass\033[1;m'
print '\033[1;33mYellow like Yolk\033[1;m'
print '\033[1;34mBlue like Blood\033[1;m'
print '\033[1;35mMagenta like Mimosa\033[1;m'
print '\033[1;36mCyan like Caribbean\033[1;m'
print '\033[1;37mWhite like Whipped Cream\033[1;m'

print '\033[1;41mHighlighted Red like Radish\033[1;m'
print '\033[1;42mHighlighted Green like Grass\033[1;m'
print '\033[1;43mHighlighted Brown like Bear\033[1;m'
print '\033[1;44mHighlighted Blue like Blood\033[1;m'
print '\033[1;45mHighlighted Magenta like Mimosa\033[1;m'
print '\033[1;46mHighlighted Cyan like Caribbean\033[1;m'
print '\033[1;47mHighlighted Gray like Ghost\033[1;m'

print ""

x = raw_input("Text: ")
print '\033[1;44m\033[1;31m{0}\033[1;m\033[1;m'.format(x)

