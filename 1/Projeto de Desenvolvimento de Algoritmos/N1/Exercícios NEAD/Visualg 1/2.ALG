Algoritmo "semnome"
// Disciplina   : [Projeto de desenvolvimento de algoritmos]
// Professor   : Rosenclever Lopes Gazoni
// Descri��o   : Considere que o �ltimo concurso vestibular apresentou tr�s provas: Portugu�s, Matem�tica e Conhecimentos Gerais. Considerando que para um candidato, tem-se um registro contendo seu nome e as notas obtidas, em cada uma das provas, construir um algoritmo que forne�a:
//a) O nome e as notas em cada prova do candidato.
//b) A m�dia do candidato.
//c) Um informa��o dizendo se o candidato foi aprovado ou n�o. Considere que um candidato � aprovado se sua m�dia for maior que 5,0 e se n�o apresentou nenhuma nota abaixo de 4,0.
// Autor(a)    : Carlos Eduardo Ferreira
// Data atual  : 03/04/2022
Var
// Se��o de Declara��es das vari�veis 
nota1, nota2, nota3, media: real
nome: caractere
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
Escreval("Digite seu nome:")
leia(nome)
Escreval("Digite sua primeira nota:")
leia(nota1)
Escreval("Digite sua segunda nota:")
leia(nota2)
Escreval("Digite sua terceira nota:")
leia(nota3)
media <- (nota1 + nota2 + nota3) / 3
se (media > 5.00) e (nota1 >= 4.00) e (nota2 >= 4.00) e (nota3 >= 4.00) entao
        escreval(nome, " voc� teve m�dia:", media, " e foi aprovado")
senao
        escreval(nome, " voc� teve m�dia:", media, " e foi reprovado")
fimse
Fimalgoritmo