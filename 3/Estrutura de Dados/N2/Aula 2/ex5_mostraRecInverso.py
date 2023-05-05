from listaEncadeada import *
from Elemento import *
from No import *

l = ListaEncadeada()

for i in range(0 ,10):
    e = Elemento()
    e.setChave(i)
    e.setNome(str(i))
    n = No(e)
    l.insereNoFim(n)

l.mostraRecInverso(l.getCabeca().getProximo())