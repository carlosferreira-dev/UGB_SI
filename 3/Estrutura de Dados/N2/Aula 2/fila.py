class Fila:

    def __init__(self):
        self.__info = []

    def filaVazia(self):
        return len(self.__info) == 0

    def enQueue(self, dado):
        self.__info.append(dado)
    
    def deQueue(self):
        if not self.filaVazia():
            return self.__info()