Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/03/2022
Var
// Se��o de Declara��es das vari�veis 
nota1, nota2, media, notafinal, mediafinal:real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite sua nota 1:")
leia(nota1)
escreval("Digite sua nota 2:")
leia(nota2)
media <- (nota1 + nota2) / 2
se media >=7.0 entao
   escreval("Voc� est� aprovado")
fimse
se media <3.5 entao
   escreval("Voc� est� reprovado")
fimse
se (media >=3.5) e (media <=6.9) entao
   escreval("Voc� est� de recupera��o, sua m�dia foi:", media)
   escreval("Voc� deve fazer um exame final")
   escreval("Digite sua nota do exame final:")
   leia(notafinal)
   mediafinal <- ((10.0 - media) + notafinal) / 2
   se mediafinal >=5.0 entao
      escreval("Aprovado com exame final, sua m�dia final foi:", mediafinal)
   senao
      escreval("Voc� ficou reprovado, sua m�dia final foi:", mediafinal)
   fimse
fimse
Fimalgoritmo