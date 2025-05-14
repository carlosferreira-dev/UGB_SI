import random
import math

#Calcula o peso total da mochila
def getPeso(peso, mochila):
    pesoAtual = 0
    for i in range(len(mochila)):
        pesoAtual += peso[i] * int(mochila[i])
    return pesoAtual

#No Subset Sum, o "valor" é o próprio peso (desde que não ultrapasse C)
def getValor(peso, mochila, C):
    soma = getPeso(peso, mochila)
    return soma if soma <= C else 0

#Gera uma mochila aleatória válida (peso ≤ C)
def geraEstadoAleatorio(peso, C):
    while True:
        estado = random.randint(0, 2 ** len(peso) - 1)
        mochila = bin(estado)[2:].zfill(len(peso))
        p = getPeso(peso, mochila)
        if p <= C:
            return mochila, p, p  # valor == peso no subset sum

#Gera vizinho aleatório com diferença de bits controlada pela "temperatura"
def geraVizinhoAleatorio(mAtual, peso, C, temperatura):
    while True:
        vizinho, p, v = geraEstadoAleatorio(peso, C)
        if getDifBits(mAtual, vizinho) <= temperatura:
            return vizinho, p, v

#Conta quantos bits diferentes entre duas soluções
def getDifBits(mAtual, mProxima):
    return sum(1 for i in range(len(mAtual)) if mAtual[i] != mProxima[i])

#Agenda de temperatura decrescente
def geraAgenda(peso, tamanho):
    n = len(peso)
    return [math.ceil(n - (tamanho - t) * n / tamanho) for t in range(tamanho, 0, -1)]

#Algoritmo principal
def simulatedAnnealing(peso, C, tamanhoAgenda):
    mAtual, pAtual, vAtual = geraEstadoAleatorio(peso, C)
    mMelhor, pMelhor, vMelhor = mAtual, pAtual, vAtual
    T = geraAgenda(peso, tamanhoAgenda)

    for t in T:
        mProx, pProx, vProx = geraVizinhoAleatorio(mAtual, peso, C, t)

        if vProx > vAtual:
            mAtual, pAtual, vAtual = mProx, pProx, vProx
            if vProx > vMelhor:
                mMelhor, pMelhor, vMelhor = mProx, pProx, vProx
        else:
            if random.random() < math.exp((vAtual - vProx) / t):
                mAtual, pAtual, vAtual = mProx, pProx, vProx

    return mMelhor, pMelhor, vMelhor

#Exemplo de uso
C = 12
peso = [4, 6, 3, 2, 7, 9, 1, 10]  # peso = valor no subset sum
mochila, pesoMochila, valorMochila = simulatedAnnealing(peso, C, 100)

print("Melhor subconjunto (binário):", mochila)
print("Itens incluídos (índices):", [i for i in range(len(mochila)) if mochila[i] == '1'])
print("Soma dos pesos:", pesoMochila)
