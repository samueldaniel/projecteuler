""" Euler Problem 2 """

def fib():
    first = 0
    second = 1
    while 1:
        n = first + second
        yield n
        first = second
        second = n

sum = 0
for i in fib():
    if i % 2 == 0:
        sum += i
    if i > 4000000:
        break

print sum
