def countup_or_countdown(x, y):
    if x > y:
        while x >= y:
            print x
            x -= 1
    else:
        while x <= y:
            print x
            x += 1

#countup_or_countdown(int(raw_input("Start: ")), int(raw_input("End: ")))

print ""

def sum0f0dds(n):
    odds = 0
    count = 0
    if n % 2 == 0:
        odds = 0
        n += 0
        count += 0
    elif n > 0:
        while n < 1000:
            print n
            n += 1
            odds += n
            count += 1
    elif n < 0:
        while n > -1000:
            print n
            n -= 1
            odds += n
            count += 1
    print "The total of all the odds is " + str(odds) + "."
    print "The number of odds is " + str(count) + "."
    print "The average of the odds is " + str(int(odds/count)) + "."

#sum0f0dds(int(raw_input("Number (From -1000 to 1000): ")))

print ""

def grid(width, height, character):
    out = ""
    while width > 0:
        out += character
        width -= 1
    return out





















print grid(int(raw_input("Width: ")), int(raw_input("Height: ")), raw_input("Character: "))
