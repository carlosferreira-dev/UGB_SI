class CrudFirebase:
    def __init__(self):
        import pyrebase
        config = {
            'apiKey': "AIzaSyBqLBA8kfIKCjcv-h6lRHIMylQxBsStNBE",
            'authDomain': "clientes-28e4a.firebaseapp.com",
            'databaseURL': "https://clientes-28e4a.firebaseio.com",
            'projectId': "clientes-28e4a",
            'storageBucket': "clientes-28e4a.appspot.com"
        }
        self.firebase = pyrebase.initialize_app(config)
        self.db = self.firebase.database()

    def lerDB(self, chave):
        if chave == '':
            user = self.db.child('usuario').get()
            return user.each()
        else:
            user = self.db.child('usuario').child(chave).get()
            return [user]

    def incluirDB(self, chave, dados):
        self.db.child('usuario').push(dados)
        self.db.child('usuario').child(chave).set(dados)
        print('Incluido com sucesso')
    
    def alterarDB(self, chave, dados):
        self.db.child('usuario').child(chave).set(dados)
        print('Alterado com sucesso')
    
    def deletarDB(self, chave):
        self.db.child('usuario').child(chave).remove()
        print('Deletado com sucesso')
    
    def ler_alunos(self, chave):
        if chave == '':
            user = self.db.child('turma_2_periodo_ugb').get()
            return user.each()
        else:
            user = self.db.child('turma_2_periodo_ugb').child(chave).get()
            return [user]