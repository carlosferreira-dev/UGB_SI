Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Ler um n�mero inteiro qualquer e multiplic�-lo por dois. Apresentar o resultado da multiplica��o somente se o resultado for maior que 30.
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
A, MULTIPLICACAO: inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
MULTIPLICACAO <- (A*2)
se MULTIPLICACAO > 30  entao
        escreval("A multiplica��o do valor de A: ",A," com 2 �: ", MULTIPLICACAO)
fimse
Fimalgoritmo