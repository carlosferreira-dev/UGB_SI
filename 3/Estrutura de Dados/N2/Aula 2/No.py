class No:
    def __init__(self, e = None):
        self.__dados = e
        self.__proximo = None

    def getDados(self):
        return self.__dados
    
    def setDados(self, d):
        self.__dados = d

    def getProximo(self):
        return self.__proximo
    
    def setProximo(self, p):
        self.__proximo = p
        
