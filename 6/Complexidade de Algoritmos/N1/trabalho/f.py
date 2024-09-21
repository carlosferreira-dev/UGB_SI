def exf(n):
    if n == 0:
        return 1
    return exf(n - 1) + exf(n - 1)

print(exf(5))
