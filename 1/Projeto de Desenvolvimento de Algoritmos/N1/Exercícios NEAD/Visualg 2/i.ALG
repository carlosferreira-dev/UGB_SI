Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Ler cinco valores num�ricos inteiros (vari�veis A, B, C, D e F), identificar e apresentar o maior e o menor valores informados. N�o execute a ordena��o dos valores como no exerc�cio "f".
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
A, B, C, D, F, MAIOR, MENOR: inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
MAIOR <- A
MENOR <- A
escreval("Digite o valor de B:")
leia(B)
se B > MAIOR entao
        MAIOR <- B
fimse
se B < MENOR entao
        MENOR <- B
fimse
escreval("Digite o valor de C:")
leia(C)
se C > MAIOR entao
        MAIOR <- C
fimse
se C < MENOR entao
        MENOR <- C
fimse
escreval("Digite o valor de D:")
leia(D)
se D > MAIOR entao
        MAIOR <- D
fimse
se D < MENOR entao
        MENOR <- D
fimse
escreval("Digite o valor de F:")
leia(F)
se F > MAIOR entao
        MAIOR <- F
fimse
se F < MENOR entao
        MENOR <- F
fimse
escreval("O maior valor digitado �: ", MAIOR," e o menor: ", MENOR)
Fimalgoritmo