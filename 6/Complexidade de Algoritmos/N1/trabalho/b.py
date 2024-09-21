def exb(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    f = [0,1]
    while len(f) < n + 1:
        nf = f[-1] + f[-2]
        f.append(nf)
    return f[len(f) -1]

print(exb(6))

#nf = f[-1]