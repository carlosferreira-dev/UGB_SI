from listaEncadeada import *
from No import *
from Elemento import *

class PilhaEncadeada(ListaEncadeada):
    def pilhaVazia(self):
        return self.listaVazia()
    
    def push(self, n):
        self.insereNoInicio(n)

    def pop(self):
        return self.retiraNoInicio()
    
p = PilhaEncadeada()
x = int(input("Digite um número natural: "))
while x > 0:
    e = Elemento()
    e.setChave(x%2)
    n = No(e)
    p.push(n)
    x = x // 2

v = ''

while not p.pilhaVazia():
    v = v + str(p.pop().getDados().getChave())
    #print(p.pop().getDados().getChave())
print(v)
