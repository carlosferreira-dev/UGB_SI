from time import time

def first_fit_modificado(itens, capacidade, pacotes_existentes):
    bins = pacotes_existentes.copy()
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

def best_fit_modificado(itens, capacidade, pacotes_existentes):
    bins = pacotes_existentes.copy()
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

def worst_fit_modificado(itens, capacidade, pacotes_existentes):
    bins = pacotes_existentes.copy()
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

#Ordena em ordem decrescente
tamanhos.sort(reverse=True)

#Separa itens > 500 (vão direto pra pacotes individuais)
pacotes_iniciais = [item for item in tamanhos if item > 500]
itens_restantes = [item for item in tamanhos if item <= 500]
print(pacotes_iniciais)
#Inicializa os pacotes com esses grandes
pacotes_base = pacotes_iniciais.copy()  #cada valor representa o tamanho inicial do pacote

#FIRST FIT
inicio = time()
total_first_fit = first_fit_modificado(itens_restantes, capacidade, pacotes_base)
tempo_first_fit = time() - inicio

#BEST FIT
inicio = time()
total_best_fit = best_fit_modificado(itens_restantes, capacidade, pacotes_base)
tempo_best_fit = time() - inicio

#WORST FIT
inicio = time()
total_worst_fit = worst_fit_modificado(itens_restantes, capacidade, pacotes_base)
tempo_worst_fit = time() - inicio

#Resultado
print("Com modificação (itens > 500 vão direto para pacotes):")
print(f"First Fit  - Pacotes usados: {total_first_fit}, Tempo: {tempo_first_fit:.4f} s")
print(f"Best Fit --- Pacotes usados: {total_best_fit}, Tempo: {tempo_best_fit:.4f} s")
print(f"Worst Fit  - Pacotes usados: {total_worst_fit}, Tempo: {tempo_worst_fit:.4f} s")