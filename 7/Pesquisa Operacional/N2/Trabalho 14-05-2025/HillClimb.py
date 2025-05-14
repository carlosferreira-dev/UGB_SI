import random

def getPeso(peso, mochila):
    pesoAtual = 0
    if len(peso) != len(mochila):
        return -1
    for i in range(0, len(mochila)):
        pesoAtual += peso[i] * int(mochila[i])
    return pesoAtual

def getValor(peso, valor, mochila, C):
    valorAtual = 0
    if len(peso) != len(mochila):
        return -1
    for i in range(0, len(mochila)):
        valorAtual += valor[i] * int(mochila[i])
    return valorAtual if getPeso(peso, mochila) <= C else (-1)*valorAtual

def geraEstadoInicial(peso, valor, C):
    estadoAtual = random.randint(0, 2 ** len(peso))
    mAtual = bin(estadoAtual)[2:].zfill(len(peso))
    pAtual = getPeso(peso, mAtual)
    while pAtual > C:
        estadoAtual = random.randint(0, 2 ** len(peso))
        mAtual = bin(estadoAtual)[2:].zfill(len(peso))
        pAtual = getPeso(peso, mAtual)
    vAtual = getValor(peso, valor, mAtual, C)
    return mAtual, pAtual, vAtual

def melhorVizinho(mAtual, peso, valor, C):
    retMochila = mAtual
    retPeso    = getPeso(peso, mAtual)
    retValor   = getValor(peso, valor, mAtual, C)
    for i in range(0, len(mAtual)):
        tMochila = ""
        for j in range(0, len(mAtual)):
            if i == j:
                tMochila = tMochila + ('0' if mAtual[j] == '1' else '1')
            else:
                tMochila = tMochila + mAtual[j]
        tPeso    = getPeso(peso, tMochila)
        tValor   = getValor(peso, valor, tMochila, C)
        if tValor > retValor:
            retMochila = tMochila
            retPeso    = tPeso
            retValor   = tValor

    return retMochila, retPeso, retValor

def subidaDeEncosta(peso, valor, C):
    mAtual, pAtual, vAtual = geraEstadoInicial(peso, valor, C)
    while True:
        mProxima, pProxima, vProxima = melhorVizinho(mAtual, peso, valor, C)
        if vProxima > vAtual:
            mAtual, pAtual, vAtual = mProxima, pProxima, vProxima
        else:
            break
    return mAtual, pAtual, vAtual

C = 12
#peso  = [4, 6, 3, 2]
#valor = [5, 7, 9, 6]
peso  = [4, 6, 3, 2, 7, 9, 1, 10]
valor = [5, 7, 9, 6, 6, 8, 10, 1]

mochila, pesoMochila, valorMochila = subidaDeEncosta(peso, valor, C)
print("Mochila", mochila)
print("Peso", pesoMochila)
print("Valor", valorMochila)