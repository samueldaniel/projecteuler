""" Euler Problem 3 """

def sieve(n):
    l = list(xrange(2, n))
    d = {}
    p = 2
    last = 0
    while p != last:
        for i in l:
            if i % p == 0:
                d[i] = -1
        yield p
        last = p
        for i in l:
            if not i in d:
                p = i
                break

def diff(a, b):
    b = set(b)
    return [aa for aa in a if aa not in b]

def sieve2(n):
    l = list(xrange(2, n))
    p = 2
    ps = []
    cs = []
    p2 = pow(p, 2)
    while p2 < n:
        ll = list(xrange(p2, n))
        for i in ll:
            if i % p == 0:
                cs.append(i)
        print ps
        ps.append(p)
        p = diff(l, cs).sort().pop()    
    return ps

print sieve2(121)

