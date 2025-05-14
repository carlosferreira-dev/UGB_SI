#Função auxiliar para calcular peso total do subconjunto
def cPeso(m, p):
    return sum(p[i] for i in m)

#Ordenação auxiliar
def selectionSort(pp, ii, inv):
    n = len(pp)
    for i in range(n-1):
        for j in range(i+1, n):
            if (inv and pp[i] < pp[j]) or (not inv and pp[i] > pp[j]):
                pp[i], pp[j] = pp[j], pp[i]
                ii[i], ii[j] = ii[j], ii[i]
    return pp, ii

#First Fit: adiciona na ordem original enquanto não ultrapassar o limite
def firstFit(peso, C):
    bm = []
    for i in range(len(peso)):
        if cPeso(bm, peso) + peso[i] <= C:
            bm.append(i)
    return bm

#Best Fit: ordena do maior para o menor (mais pesado primeiro)
def bestFit(peso, C):
    pp = peso.copy()
    ii = list(range(len(peso)))
    pp, ii = selectionSort(pp, ii, True)  # ordem decrescente
    bm = []
    for i in range(len(pp)):
        if cPeso(bm, pp) + pp[i] <= C:
            bm.append(i)
    # recuperar índices originais
    ret = [ii[i] for i in bm]
    return ret

#Worst Fit: ordena do menor para o maior (mais leve primeiro)
def worstFit(peso, C):
    pp = peso.copy()
    ii = list(range(len(peso)))
    pp, ii = selectionSort(pp, ii, False)  # ordem crescente
    bm = []
    for i in range(len(pp)):
        if cPeso(bm, pp) + pp[i] <= C:
            bm.append(i)
    # recuperar índices originais
    ret = [ii[i] for i in bm]
    return ret

#Exemplo de uso:
C = 12
peso = [4, 6, 3, 2]

#Troque aqui para testar cada algoritmo:
res = firstFit(peso, C)
#res = bestFit(peso, C)
#res = worstFit(peso, C)

print("Índices selecionados:", res)
print("Subconjunto:", [peso[i] for i in res])
print("Soma total:", cPeso(res, peso))
