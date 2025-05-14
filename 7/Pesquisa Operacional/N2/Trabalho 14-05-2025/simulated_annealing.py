import random
import math

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

def geraEstadoAleatorio(peso, valor, C):
    estadoAtual = random.randint(0, 2 ** len(peso))
    mAtual = bin(estadoAtual)[2:].zfill(len(peso))
    pAtual = getPeso(peso, mAtual)
    while pAtual > C:
        estadoAtual = random.randint(0, 2 ** len(peso))
        mAtual = bin(estadoAtual)[2:].zfill(len(peso))
        pAtual = getPeso(peso, mAtual)
    vAtual = getValor(peso, valor, mAtual, C)
    return mAtual, pAtual, vAtual

def geraVizinhoAleatorio(mAtual, peso, valor, C, temperatura):
    retMochila, retPeso, retValor = geraEstadoAleatorio(peso, valor, C)
    while getDifBits(mAtual, retMochila) > temperatura:
      retMochila, retPeso, retValor = geraEstadoAleatorio(peso, valor, C)
    return retMochila, retPeso, retValor

def getDifBits(mAtual, mProxima):
    diferenca = 0
    if len(mAtual) != len(mProxima):
        return len(mAtual) + 1
    for i in range(0, len(mAtual)):
        if mAtual[i] != mProxima[i]:
            diferenca += 1
    return diferenca

def geraAgenda(peso, tamanho):
  n = len(peso)
  T = []
  for t in range(tamanho, 0, -1):
    T.append(math.ceil(n-(tamanho-t)*n/tamanho))
  return T

def simulatedAnnealing(peso, valor, C, tamanhoAgenda):
    mAtual, pAtual, vAtual = geraEstadoAleatorio(peso, valor, C)
    mMelhor, pMelhor, vMelhor = mAtual, pAtual, vAtual
    T = geraAgenda(peso, tamanhoAgenda)
    for t in T:
        mProxima, pProxima, vProxima = geraVizinhoAleatorio(mAtual, peso, valor, C, t)
        if vProxima > vAtual:
            mAtual, pAtual, vAtual = mProxima, pProxima, vProxima
            if vProxima > vMelhor:
                mMelhor, pMelhor, vMelhor = mProxima, pProxima, vProxima
        else:
            if random.random() < math.exp((vAtual - vProxima) / t):
                mAtual, pAtual, vAtual = mProxima, pProxima, vProxima
    return mMelhor, pMelhor, vMelhor

C = 12
peso  = [4, 6, 3, 2, 7, 9, 1, 10]
valor = [5, 7, 9, 6, 6, 8, 10, 1]
mochila, pesoMochila, valorMochila = simulatedAnnealing(peso, valor, C, 100)
print("Mochila", mochila)
print("Peso", pesoMochila)
print("Valor", valorMochila)



