Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Efetuar a leitura de um nome (vari�vel NOME) e o sexo (vari�vel SEXO) de uma pessoa e apresentar como sa�da uma das seguintes mensagens: "Ilmo. Sr.", caso seja informado o sexo masculino (utilizar como valor o caractere "M"), ou "Ilma. Sra.", caso seja informado o sexo feminino (utilizar como valor o caractere "F"). Ap�s a mensagem de sauda��o, apresentar o nome informado. O programa deve, ap�s a entrada do sexo, verificar primeiramente se o sexo fornecido � realmente v�lido, ou seja, se � igual a "M" ou a "F". N�o sendo essa condi��o verdadeira, o programa deve apresentar a mensagem "Sexo informado inv�lido".
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
NOME, SEXO: caractere
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite seu nome:")
leia(NOME)
escreval("Qual seu sexo? MASCULINO(M ou m) / FEMININO(F ou f)")
leia(SEXO)
se (SEXO = "M") ou (SEXO = "m") ou (SEXO = "F") ou (SEXO = "f") entao
        se (SEXO = "M") ou (SEXO = "m") entao
                escreval("Sr. ", nome)
        senao
                escreval("Sra. ", nome)
        fimse
senao
        escreval("Sexo informado � inv�lido")
fimse
Fimalgoritmo