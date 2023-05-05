from listaEncadeada import *
from No import *
from Elemento import *

class FilaEncadeada(ListaEncadeada):
    def pilhaVazia(self):
        return self.listaVazia()
    
    def push(self, n):
        self.insereNoInicio(n)

    def pop(self):
        return self.retiraNoFim()
    
f = FilaEncadeada()
x = int(input("Digite um número natural: "))
while x > 0:
    e = Elemento()
    e.setChave(x%2)
    n = No(e)
    f.push(n)
    x = x // 2
    
while not f.pilhaVazia():
    print(f.pop().getDados().getChave())
