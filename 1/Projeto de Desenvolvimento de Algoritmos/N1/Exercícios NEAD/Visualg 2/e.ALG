Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Efetuar a leitura de tr�s valores num�ricos (representados pelas vari�veis A, B e C) e processar o c�lculo da equa��o completa de segundo grau, utilizando a f�rmula de Bhaskara (considerar para a solu��o do problema todas as poss�veis condi��es para delta: delta < 0 � n�o h� solu��o real, delta > 0 � h� duas solu��es reais e diferentes e delta = 0 � h� apenas uma solu��o real). Lembre- -se de que � completa a equa��o de segundo grau que possui todos os coeficientes A, B e C diferentes de zero. O programa deve apresentar respostas para todas as condi��es estabelecidas para delta.
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
A, B, C, DELTA, X1, X2: real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite o valor de A:")
leia(A)
escreval("Digite o valor de B:")
leia(B)
escreval("Digite o valor de C:")
leia(C)
DELTA <- ((B*B) - 4*A*C)
se DELTA < 0 entao
        escreval("N�o h� solu��o real")
senao
        se DELTA = 0 entao
                X1 <- -B / (2*A)
                escreval("H� apenas uma solu��o real, X: ",X1)
        senao
                X1 <- (-B + RAIZQ(DELTA)) / (2*A)
                X2 <- (-B - RAIZQ(DELTA)) / (2*A)
                escreval("H� duas solu��es reais e diferentes: X1: ",X1," X2: ", X2)
        fimse
fimse
Fimalgoritmo