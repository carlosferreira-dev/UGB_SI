Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Escreva um algoritmo que, para uma conta banc�ria, leia seu n�mero, o saldo, o tipo de opera��o a ser realizada (dep�sito ou saque) e o valor da opera��o. Ap�s, determine e mostre o novo saldo. Se o novo saldo ficar negativo, deve ser mostrada tamb�m a mensagem 'Conta estourada'.
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
conta: inteiro
operacao: caractere
saldo, valorop: real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite o n�mero da sua conta:")
leia(conta)
escreval("Digite seu saldo atual:")
leia(saldo)
escreval("Qual opera��o voc� quer efetuar? SAQUE(S) ou DEPOSITO(D)")
leia(operacao)
se (operacao = "S") ou (operacao = "s") entao
        escreval("Qual valor voc� quer sacar?")
        leia(valorop)
        saldo <- saldo - valorop
        se saldo < 0.00 entao
                escreval("Sua conta: ",conta," ficou estourada, com saldo: ", saldo)
        senao
                escreval("Opera��o realizada com sucesso, seu novo saldo �: ", saldo)
        fimse
senao
        escreval("Qual valor voc� quer depositar?")
        leia(valorop)
        saldo <- saldo + valorop
        escreval("Opera��o relizada com sucesso, seu novo saldo �: ", saldo)
fimse
Fimalgoritmo