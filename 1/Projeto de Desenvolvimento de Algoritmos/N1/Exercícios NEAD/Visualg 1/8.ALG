Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Escreva um algoritmo que calcule o valor do imposto de renda de um contribuinte. Considere que o valor do imposto � calculado de acordo com a tabela abaixo:
//at� R$10.000,00 / ALIQUOTA ISENTO / DEDU��O 0
// > que R$10.000,00 e <= R$ 25.000,00 / ALIQUOTA 10% / DEDU��O 1000
// > R$ 25.000,00 / ALIQUOTA 25% / DEDU��O 4750
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
renda, imposto: real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite o valor da sua renda anual:")
leia(renda)
se renda <= 10000.00 entao
        escreval("Voc� est� isento de imposto")
senao
        se (renda > 10000.00) e (renda <=25000.00) entao
                imposto <- (renda * 0.10) - 1000
                escreval("Seu imposto com 10% de aliquota foi: ", imposto:2:2)
        senao
                imposto <- (renda * 0.25) - 4750
                escreval("Seu imposto com 25% de aliquota foi: ", imposto:2:2)
        fimse
fimse
Fimalgoritmo