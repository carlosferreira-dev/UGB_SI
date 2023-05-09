from No import No

class ListaEncadeada:
    def __init__(self):
        self.__cabeca = No()

    def listaVazia(self):
        return self.__cabeca.getProximo() == None
    
    def getCabeca(self):
        return self.__cabeca
    
    def setCabeca(self, valor):
        self.__cabeca = valor

    def insereNoInicio(self, n):
        n.setProximo(self.getCabeca().getProximo())
        self.getCabeca().setProximo(n)

    def retiraNoInicio(self):
        ret = None
        if not self.listaVazia():
            ret = self.getCabeca().getProximo()
            self.getCabeca().setProximo(ret.getProximo())
            ret.setProximo(None)
        return ret
    
    def insereOrdenado(self, n):
        ant = self.getCabeca()
        atu = self.getCabeca().getProximo()
        while atu != None and atu.getDados().getChave() < n.getDados().getChave():
            ant = atu
            atu = atu.getProximo()
        ant.setProximo(n)
        n.setProximo(atu)

    def inserenaPosicao(self, n, p):
        tamanho = self.getTamanho()
        ant = self.getCabeca()
        atu = self.getCabeca().getProximo()
        if p == atu:
            ant = self.getCabeca().setProximo(n)
            atu =  


    def retiraElemento(self, x):
        ret = None
        if not self.listaVazia():
            ant = self.getCabeca()
            atu = self.getCabeca().getProximo()
            while atu != None and atu.getDados().getChave() != x:
                ant = atu
                atu = atu.getProximo()
            if atu != None:
                ant.setProximo(atu.getProximo())
                atu.setProximo(None)
            ret = atu
        return ret

    def retiraNoFim(self):
        ret = None
        if not self.listaVazia():
            ant = self.getCabeca()
            atual = self.getCabeca().getProximo()
            while atual.getProximo() != None:
                ant = atual
                atual = atual.getProximo()
            ret = atual
            ant.setProximo(None)
        return ret

    def insereNoFim(self, n):
        ant = self.getCabeca()
        atual = self.getCabeca().getProximo()
        while atual != None:
            ant = atual
            atual = atual.getProximo()
        ant.setProximo(n)                

    def mostraLista(self):
        atual = self.getCabeca().getProximo()
        while atual != None:
            print(atual.getDados().getValores())
            atual = atual.getProximo()

    def getTamanho(self):
        ret = 0
        atu = self.getCabeca().getProximo()
        while atu != None:
            ret = ret + 1
            atu = atu.getProximo()
        return ret
    
    def mostraRec(self, n):
        if n != None:
            print(n.getDados().getValores())
            self.mostraRec(n.getProximo())

    def mostraRecInverso(self, n):
        if n != None:
            self.mostraRec(n.getProximo())
            print(n.getDados().getValores())