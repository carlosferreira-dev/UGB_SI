#Função de avaliação: soma apenas se não ultrapassar o alvo T
def calcSubsetSum(p, T, vet):
    soma = sum(p[i] for i in vet)
    return soma if soma <= T else soma * (-1)

#Busca exaustiva por divisão e conquista
def subsetSumExato(p, a, T, vet):
    if a == len(p):
        return vet
    else:
        l = vet[:]        #Não inclui o elemento atual
        r = vet[:]        
        r.append(a)       #Inclui o elemento atual

        vetl = subsetSumExato(p, a+1, T, l)
        vetr = subsetSumExato(p, a+1, T, r)

        vl = calcSubsetSum(p, T, vetl)
        vr = calcSubsetSum(p, T, vetr)

        #Preferência para o subconjunto com soma mais próxima de T (sem ultrapassar)
        return vetl if vl > vr else vetr

#Exemplo:
T = 12
p = [4, 6, 3, 2, 7, 9, 1, 10]   #conjunto de entrada
m = [0 for _ in range(len(p))]

#executa
vet = subsetSumExato(p, 0, T, [])

#exibe resultado
print("Índices do subconjunto:", vet)
print("Subconjunto:", [p[i] for i in vet])
print("Soma:", sum(p[i] for i in vet))

#marca com 1 os elementos selecionados
for i in vet:
    m[i] = 1
print("Máscara de seleção:", m)
