Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Fa�a um algoritmo que tome como entrada dois valores inteiros e determine se s�o m�ltiplos um do outro, ou n�o.
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
A, B:inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
escreval("Digite o valor de B:")
leia(B)
se (A MOD B = 0) ou (B MOD A = 0) entao
        escreval("Os valores de A e B s�o m�ltiplos")
senao
        escreval("Os valores de A e B n�o s�o m�ltiplos")
fimse
Fimalgoritmo