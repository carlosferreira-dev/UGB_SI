Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Fazer a leitura de quatro valores num�ricos inteiros representados pelas vari�veis A, B, C e D. Apresentar apenas os valores que sejam divis�veis por 2 e 3.
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
A, B, C, D: inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
escreval("Digite o valor de B:")
leia(B)
escreval("Digite o valor de C:")
leia(C)
escreval("Digite o valor de D:")
leia(D)
se (A MOD 2 = 0) e (A MOD 3 = 0) entao
        escreval("O valor de A: ",A," � divis�vel por 2 e 3")
fimse
se (B MOD 2 = 0) e (B MOD 3 = 0) entao
        escreval("O valor de B: ",B," � divis�vel por 2 e 3")
fimse
se (C MOD 2 = 0) e (C MOD 3 = 0) entao
        escreval("O valor de C: ",C," � divis�vel por 2 e 3")
fimse
se (D MOD 2 = 0) e (D MOD 3 = 0) entao
        escreval("O valor de D: ",D," � divis�vel por 2 e 3")
fimse
Fimalgoritmo