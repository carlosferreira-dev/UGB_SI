from NoABB import No
class ArvoreBuscaBinaria:
    def __init__(self):
        self.__raiz = None
    def getRaiz(self):
        return self.__raiz
    def setRaiz(self, n):
        self.__raiz = n
    def arvoreVazia(self):
        return self.__raiz == None
    def criaNo(self, v):
        no = No()
        no.getDados().setChave(v)
        return no
    def insereNo(self, v):
        if self.arvoreVazia():
            self.setRaiz(self.criaNo(v))
        else:
            self.insere(None, self.getRaiz(), v)
    def insere(self, pai, atual, v):
        if atual != None:
            if v < atual.getDados().getChave(): # Alteração do elemento
                self.insere(atual, atual.getFilhoEsquerda(), v)
            else:
                self.insere(atual, atual.getFilhoDireita(), v)
        else:
            x = self.criaNo(v)
            if v < pai.getDados().getChave():
                pai.setFilhoEsquerda(x)
            else:
                pai.setFilhoDireita(x)
    def emOrdem(self, n):
        if n != None:
            self.emOrdem(n.getFilhoEsquerda())
            print(n.getDados().getChave())
            self.emOrdem(n.getFilhoDireita())
    
    def preOrdem(self, n):
        if n != None:
            print(n.getDados().getChave())
            self.preOrdem(n.getFilhoEsquerda())
            self.preOrdem(n.getFilhoDireita())

    def posOrdem(self, n):
        if n != None:
            self.posOrdem(n.getFilhoEsquerda())
            self.posOrdem(n.getFilhoDireita())
            print(n.getDados().getChave())
        

    #Exercício 1
    #Apresente os elementos em ordem decrescente
    def decrescente(self, n):
        if n != None:
            self.decrescente(n.getFilhoDireita())
            print(n.getDados().getChave())
            self.decrescente(n.getFilhoEsquerda())

    #Exercício 2
    def pesquisa(self, n, v):
        if n != None:
            if v == n.getDados().getChave():
                return True
            elif v < n.getDados().getChave():
                return self.pesquisa(n.getFilhoEsquerda(), v)
            else:
                return self.pesquisa(n.getFilhoDireita(), v)
        return False

    #Exercício 3
    def qtd(self, n):
        if n != None:
            return 1 + self.qtd(n.getFilhoEsquerda()) + self.qtd(n.getFilhoDireita())
        return 0

    #Desafio
    #Transforme o código do exercício 3 em uma 1 linha
    def qtd_desafio(self, n):
        return 0 if n == None else 1  + self.qtd(n.getFilhoEsquerda()) + self.qtd(n.getFilhoDireita())
    
    #Exercício 4
    def soma(self, n):
        if n != None:
            return n.getDados().getChave() + self.soma(n.getFilhoEsquerda()) + self.soma(n.getFilhoDireita())
        return 0

    #Exercício 5
    def menor(self, n):
        if n != None:
            self.menor(n.getFilhoEsquerda())
        return n.get

arv = ArvoreBuscaBinaria()

k = [15,8,11,5,1,7,20,22,17,16,18]
for i in k:
  arv.insereNo(i)

#Exercício 1
#arv.decrescente(arv.getRaiz())

#Exercício 2
#print(arv.pesquisa(arv.getRaiz(), 8))

#Exercício 3
#print(arv.qtd(arv.getRaiz()))

#Desafio
#print(arv.qtd_desafio(arv.getRaiz()))

#Exercício 4
print(arv.soma(arv.getRaiz()))