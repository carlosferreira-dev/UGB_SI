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

ch = int(input("Digite uma chave (-1 Para encerrar): "))
while ch != -1 and not l.listaVazia():
    ret = l.retiraElemento(ch)
    if ret != None:
        print("Elemento retirado: ", ret.getDados().getValores())
    else:
        print("Chave não encontrada!")
    l.mostraLista()
    ch = int(input("Digite uma chave (-1 Para encerrar): "))
