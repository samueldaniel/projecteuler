""" Euler Problem 25"""

def fib():
    first = 0
    second = 1
    while 1:
        n = first + second
        yield n
        first = second
        second = n

counter = 2
for i in fib():
    if len(str(i)) == 1000:
        print counter
        break
    else:
        counter += 1
