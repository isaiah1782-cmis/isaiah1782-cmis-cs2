a = int(raw_input("Starting number: "))

b = int(raw_input("Ending number: "))

def countdown(start, stop):
    if a == b or a >= b:
        print 'Blastoff!'
    else:
        print a
        (countdown(a+1))

countdown(a, b)
