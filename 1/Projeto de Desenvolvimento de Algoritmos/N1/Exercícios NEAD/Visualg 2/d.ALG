Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Ler os valores de quatro notas escolares bimestrais de um aluno representadas pelas vari�veis N1, N2, N3 e N4. Calcular a m�dia aritm�tica (vari�vel MD1) desse aluno e apresentar a mensagem "Aprovado" se a m�dia obtida for maior ou igual a 7; caso contr�rio, o programa deve solicitar a quinta nota (nota de exame, representada pela vari�vel NE) do aluno e calcular uma nova m�dia aritm�tica (vari�vel MD2) entre a nota de exame e a primeira m�dia aritm�tica. Se o valor da nova m�dia for maior ou igual a cinco, apresentar a mensagem "Aprovado em exame"; caso contr�rio, apresentar a mensagem "Reprovado". Informar tamb�m, ap�s a apresenta��o das mensagens, o valor da m�dia obtida pelo aluno.
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
N1, N2, N3, N4, NE, MD1, MD2: real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite o valor da nota 1:")
leia(N1)
escreval("Digite o valor da nota 2:")
leia(N2)
escreval("Digite o valor da nota 3:")
leia(N3)
escreval("Digite o valor da nota 4:")
leia(N4)
MD1 <- (N1 + N2 +N3 +N4) / 4
se MD1 >= 7.00 entao
        escreval("Aprovado com m�dia: ", MD1)
senao
        escreval("Reprovado com m�dia: ", MD1, " Digite a nota de exame: ")
        leia(NE)
        MD2 <- (NE + MD1) / 2
        se MD2 >= 5.00 entao
                escreval("Aprovado com m�dia: ", MD2)
        senao
                escreval("Reprovado com m�dia: ", MD2)
        fimse
fimse
Fimalgoritmo