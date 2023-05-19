from Elemento import Elemento
class No:
    def __init__(self):
        self.__dados = Elemento() # Alterei aqui
        self.__filhoEsquerda = None
        self.__filhoDireita = None
    def getFilhoEsquerda(self):
        return self.__filhoEsquerda
    def setFilhoEsquerda(self, n):
        self.__filhoEsquerda = n
    def getFilhoDireita(self):
        return self.__filhoDireita
    def setFilhoDireita(self, n):
        self.__filhoDireita = n
    def getDados(self): # Mudei o nome do Método
        return self.__dados
    def setDados(self, d): # Mudei o nome do Método
        self.__dados = d