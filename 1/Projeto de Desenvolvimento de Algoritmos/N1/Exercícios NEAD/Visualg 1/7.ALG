Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : O sistema de avalia��o de determinada disciplina, � composto por tr�s provas. A primeira prova tem peso 2, a segunda tem peso 4 e a terceira tem peso 6. Fa�a um algoritmo para calcular a m�dia de um aluno desta disciplina.
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
N1, N2, N3, MEDIA: real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite o valor da nota 1 com peso 2:")
leia(N1)
escreval("Digite o valor da nota 2 com peso 4:")
leia(N2)
escreval("Digite o valor da nota 3 com peso 6:")
leia(N3)
MEDIA <- ((N1 * 2) + (N2 * 4) + (N3 * 6)) / 12
escreval("A m�dia foi: ", MEDIA)
Fimalgoritmo