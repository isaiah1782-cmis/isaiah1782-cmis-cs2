n = int(raw_input("Count: "))

def countdown(n):
    if n == 10 or n >= 10:
        print 'Blastoff!'
    else:
        print n
        (countdown(n+1))

countdown(n)
