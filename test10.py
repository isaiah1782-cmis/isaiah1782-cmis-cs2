def collatz_sequence(x):
    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
         print x
       else:
         x = 3 * x + 1
         print x 
       seq.append(x)
    return seq

collatz_sequence(int(raw_input("Number: ")))
