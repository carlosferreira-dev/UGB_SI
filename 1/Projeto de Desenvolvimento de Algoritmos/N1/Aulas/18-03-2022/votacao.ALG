Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/03/2022
Var
// Se��o de Declara��es das vari�veis 
idade:inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Digite sua idade para saber se voc� deve votar nessa elei��o.")
leia(idade)
se (idade >= 18) e (idade <=60) entao
   escreval("O voto � obrigat�rio!")
senao
     se (idade >=16)  e (idade <=17) entao
        escreval("O voto � opcional.")
     senao
     fimse
          se idade < 16 entao
             escreval("N�o � permitido votar!")
          senao
          fimse
               se idade >=61 entao
               escreval("O voto n�o � mais obrigat�rio.")
               fimse
fimse
Fimalgoritmo