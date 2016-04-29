n0 = float(raw_input("n0: "))
n1 = float(raw_input("n1: "))
n2 = float(raw_input("n2: "))
n3 = float(raw_input("n3: "))
n4 = float(raw_input("n4: "))

def x():
    if n0 < 0 and n0 >= 10:
        print "k"


l = [n0, n1, n2, n3, n4]
print reduce(lambda x, y: x + y, l) / len(l)
