class Elemento:
	def __init__(self):
		self.__chave = 0
		self.__nome = ""

	def getChave(self):
		return self.__chave

	def setChave(self, valor):
		self.__chave = valor

	def getNome(self):
		return self.__nome

	def setNome(self, n):
		self.__nome = n

	def getValores(self):
		return self.__chave, self.__nome