from listaEncadeada import *
from Elemento import *
from No import *

l = ListaEncadeada()
ch = int(input("Digite uma chave (-1 Para encerrar): "))
while ch != -1:
    nome = input("Digite um nome: ")
    e = Elemento()
    e.setChave(ch)
    e.setNome(nome)
    n = No(e)
    l.insereNoInicio(n)
    l.mostraLista()
    ch = int(input("Digite uma chave (-1 Para encerrar): "))

while not l.listaVazia():
    print(l.retiraNoInicio().getDados().getValores())