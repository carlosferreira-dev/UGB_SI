def alg1a(n):
    if n==1 or n==2:
        return 1
    else:
        return alg1a(n-2)+alg1a(n-1)
