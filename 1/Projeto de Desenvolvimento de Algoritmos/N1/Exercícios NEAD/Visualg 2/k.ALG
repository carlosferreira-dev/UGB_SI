Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Efetuar a leitura de um valor num�rico inteiro que esteja na faixa de valores de 1 at� 9. O programa deve apresentar a mensagem "O valor est� na faixa permitida", caso o valor informado esteja entre 1 e 9. Se o valor estiver fora da faixa, o programa deve apresentar a mensagem "O valor est� fora da faixa permitida".
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
A: inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
se (A >= 1) e (A <= 9) entao
        escreval("O valor est� na faixa permitida")
senao
        escreval("O valor est� fora da faixa permitida")
fimse
Fimalgoritmo