def balde(x):
    qtdBaldes = len(x)
    baldes = [[] for _ in range(qtdBaldes)]
    for num in x:
        index = num - 1
        baldes[index].append(num)
        print(baldes, f'Index atual: {baldes[index]}')
    
    x = []
    for balde in baldes:
        print(f'X ANTES DO EXTEND {x}')
        x.extend(balde)
        print(f'X depois DO EXTEND {x}')
    return x

print(balde([2,4,1,1,2,3,2,7,4,6]))

#10 vezes no primeiro FOR + 10 vezes no segundo FOR = 2n = corta constantes = n
# Complexidade de tempo O(n)
# Complexidade de espaço 