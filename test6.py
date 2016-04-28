x = raw_input("Number: ")
n = raw_input("Power: ")

def pow(x, n):
    if x == 0: return 0
    elif n == 0: return 1
    elif n == 0: return x
    elif n % 2 == 0:
        even = pow(x, n/2)
        return even * even
    else:
        n = (n-1)/2
        odd = pow(x, n)
        return x * odd * odd

print pow(float(x), float(n))
