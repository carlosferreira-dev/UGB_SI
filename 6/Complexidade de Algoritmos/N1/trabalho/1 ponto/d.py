def exd(x,y):
    r = 0
    while y > 0:
        if y % 2 == 1: #Resto da divisão
            r = r + x
        x = x + x
        y = y // 2 #Valor inteiro da divisão
    return r

print(exd(5,6))

# 6 % 2 = 0
# x = 5 + 5 = 10
# y = 6 // 2 = y = 3

# 3 % 2  == 1
# r = 0 + 10
# x = 10 + 10 = 20
# y = 3 // 2 = 1
# r = 10 + 20 = 30