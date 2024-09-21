def alg1b(n):
    ant = 0
    pos = 1
    n = n-1
    while n>=1:
        print(n)
        t = ant
        ant = pos
        pos = pos + t
        n = n-1
    return pos
