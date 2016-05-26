def countup_or_countdown(x, y):
    if x > y:
        while x >= y:
            print x
            x -= 1
    else:
        while x <= y:
            print x
            x += 1

countup_or_countdown(int(raw_input("Start: ")), int(raw_input("End: ")))

print ""

def sum0f0dds(n):
    while n % 2 == 0:
        continue #WRONG
    if n > 0:
        while n < 1000:
            print n
            n += 1
    if n < 0:
        while n > -1000:
            print n
            n +- 1

sum0f0dds(int(raw_input("Number: ")))
