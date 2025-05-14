def selectionSort(pp, vv, ii, inv):
    n = len(pp)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if (inv and pp[i] < pp[j]) or (not inv and pp[i] > pp[j]):
                pp[i], pp[j] = pp[j], pp[i]
                vv[i], vv[j] = vv[j], vv[i]
                ii[i], ii[j] = ii[j], ii[i]
    return pp, vv, ii

def cPeso(m, p):
    r = 0
    for i in m:
        r = r + p[i]
    return r

def cValor(m, v, p, C):
    r = 0
    for i in m:
        r = r + v[i]
    return r if cPeso(m, p)<= C else r*(-1)

def firstFit(bm, peso, valor, n, C):
    for i in range(n):
        if cPeso(bm, peso) + peso[i] <= C:
            bm.append(i)
    return bm

def bestFit(bm, peso, valor, n, C):
    pp = peso.copy()
    vv = valor.copy()
    ii = [i for i in range(len(peso))]
    pp, vv, ii = selectionSort(pp, vv, ii, True)
    for i in range(n):
        if cPeso(bm, pp) + pp[i] <= C:
            bm.append(i)
    ret = []
    for i in bm:
        ret.append(ii[i])
    return ret

def worstFit(bm, peso, valor, n, C):
    pp = peso.copy()
    vv = valor.copy()
    ii = [i for i in range(len(peso))]
    pp, vv, ii = selectionSort(pp, vv, ii, False)
    print(pp, vv)
    for i in range(n):
        if cPeso(bm, pp) + pp[i] <= C:
            bm.append(i)
    ret = []
    for i in bm:
        ret.append(ii[i])
    return ret

C = 12
peso  = [4, 6, 3, 2]
valor = [5, 7, 9, 6]
bm = []
bm = worstFit(bm, peso, valor, len(peso), C)
#bm = bestFit(bm, peso, valor, len(peso), C)
#bm = firstFit(bm, peso, valor, len(peso), C)
print(bm, "Valor: ", cValor(bm, valor, peso, C), "Peso: ", cPeso(bm, peso))