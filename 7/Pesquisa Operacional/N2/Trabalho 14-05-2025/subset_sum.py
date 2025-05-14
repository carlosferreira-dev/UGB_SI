import pulp

def subset_sum_solver(pesos, capacidade):
    n = len(pesos)

    # Define o problema de otimização
    prob = pulp.LpProblem("Subset_Sum", pulp.LpMaximize)

    # Cria variáveis binárias x0, x1, ..., xn-1
    x = [pulp.LpVariable(f"x{i}", cat='Binary') for i in range(n)]

    # Função objetivo: maximizar a soma dos pesos incluídos
    prob += pulp.lpSum(pesos[i] * x[i] for i in range(n)), "Valor_total"

    # Restrição: peso total não pode ultrapassar a capacidade
    prob += pulp.lpSum(pesos[i] * x[i] for i in range(n)) <= capacidade, "Restrição_capacidade"

    # Resolve o problema
    prob.solve()

    # Resultados
    itens_incluidos = [i for i in range(n) if x[i].value() == 1]
    peso_total = sum(pesos[i] for i in itens_incluidos)

    return itens_incluidos, peso_total

# Exemplo
pesos = [4, 6, 3, 2, 7, 9, 1, 10]
capacidade = 12

itens, peso = subset_sum_solver(pesos, capacidade)

print("Itens incluídos (índices):", itens)
print("Soma dos pesos:", peso)
