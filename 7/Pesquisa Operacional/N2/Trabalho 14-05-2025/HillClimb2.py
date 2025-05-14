import random

#Calcula o peso total dos itens na mochila (mochila representada por string binária)
def getPeso(peso, mochila):
    pesoAtual = 0
    for i in range(len(mochila)):
        pesoAtual += peso[i] * int(mochila[i])
    return pesoAtual

#Para o Subset Sum, o valor é o próprio peso total se for válido, senão é 0
def getValor(peso, mochila, C):
    soma = getPeso(peso, mochila)
    return soma if soma <= C else 0

#Gera uma solução inicial aleatória válida (não ultrapassa C)
def geraEstadoInicial(peso, C):
    while True:
        estado = random.randint(0, 2 ** len(peso) - 1)
        mochila = bin(estado)[2:].zfill(len(peso))
        if getPeso(peso, mochila) <= C:
            return mochila, getPeso(peso, mochila)

#Gera os vizinhos (tenta ligar ou desligar cada item) e escolhe o melhor
def melhorVizinho(mAtual, peso, C):
    melhorMochila = mAtual
    melhorPeso = getValor(peso, mAtual, C)

    for i in range(len(mAtual)):
        vizinho = list(mAtual)
        vizinho[i] = '0' if mAtual[i] == '1' else '1'
        vizinho = ''.join(vizinho)
        pesoVizinho = getValor(peso, vizinho, C)

        if pesoVizinho > melhorPeso:
            melhorMochila = vizinho
            melhorPeso = pesoVizinho

    return melhorMochila, melhorPeso

#Executa a busca da subida de encosta
def subidaDeEncosta(peso, C):
    mAtual, pAtual = geraEstadoInicial(peso, C)

    while True:
        mVizinho, pVizinho = melhorVizinho(mAtual, peso, C)
        if pVizinho > pAtual:
            mAtual, pAtual = mVizinho, pVizinho
        else:
            break

    return mAtual, pAtual

#Exemplo de uso
C = 12
peso = [4, 6, 3, 2, 7, 9, 1, 10]  # valores iguais aos pesos no Subset Sum

mochila, soma = subidaDeEncosta(peso, C)
print("Melhor subconjunto (binário):", mochila)
print("Itens incluídos (índices):", [i for i in range(len(mochila)) if mochila[i] == '1'])
print("Soma dos pesos:", soma)
