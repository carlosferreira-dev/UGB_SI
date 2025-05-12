from time import time

def first_fit(itens, capacidade):
    bins = []
    for item in itens:
        colocado = False
        for i in range(len(bins)):
            if bins[i] + item <= capacidade:
                bins[i] += item
                colocado = True
                break
        if not colocado:
            bins.append(item)
    return len(bins)

def best_fit(itens, capacidade):
    bins = []
    for item in itens:
        melhor = -1
        menor_espaco = capacidade + 1
        for i in range(len(bins)):
            espaco_restante = capacidade - bins[i]
            if espaco_restante >= item and espaco_restante < menor_espaco:
                melhor = i
                menor_espaco = espaco_restante
        if melhor != -1:
            bins[melhor] += item
        else:
            bins.append(item)
    return len(bins)

def worst_fit(itens, capacidade):
    bins = []
    for item in itens:
        pior = -1
        maior_espaco = -1
        for i in range(len(bins)):
            espaco_restante = capacidade - bins[i]
            if espaco_restante >= item and espaco_restante > maior_espaco:
                pior = i
                maior_espaco = espaco_restante
        if pior != -1:
            bins[pior] += item
        else:
            bins.append(item)
    return len(bins)

with open("binPacking10000.csv", "r") as f:
    linhas = f.readlines()

capacidade = int(linhas[0].strip())
tamanhos = [int(l.strip()) for l in linhas[1:]]

#FIRST FIT
inicio = time()
bins_first_fit = first_fit(tamanhos, capacidade)
tempo_first_fit = time() - inicio

#BEST FIT
inicio = time()
bins_best_fit = best_fit(tamanhos, capacidade)
tempo_best_fit = time() - inicio

#WORST FIT
inicio = time()
bins_worst_fit = worst_fit(tamanhos, capacidade)
tempo_worst_fit = time() - inicio

#Resultado
print("binPacking10000.csv")
print(f"First Fit  - Bins usados: {bins_first_fit}, Tempo: {tempo_first_fit:.4f} s")
print(f"Best Fit --- Bins usados: {bins_best_fit}, Tempo: {tempo_best_fit:.4f} s")
print(f"Worst Fit  - Bins usados: {bins_worst_fit}, Tempo: {tempo_worst_fit:.4f} s")