Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Fazer a leitura de um valor num�rico inteiro qualquer e apresent�-lo caso n�o seja maior que 3. Dica: para a solu��o deste problema utilize apenas o operador l�gico de nega��o.
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
A: inteiro
solucao: logico
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
solucao <- nao (A >=3 )
escreval("O valor digitado de A: ",A," n�o � maior do que 3. ", solucao)
Fimalgoritmo