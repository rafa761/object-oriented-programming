<<<<<<< Updated upstream
#__str__
class Conta(object):
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def __str__(self): #Esse metodo especial transforma a classe em uma string
        return f'ID: {self.idConta}\nSaldo: R${self.saldo}'

viacredi = Conta(123, 5000)
print(viacredi)

#__add__
class Conta2(object):
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def __add__(self, valor):
        self.saldo += valor

nubank = Conta2(456, 1000)
nubank.__add__(50)
print(nubank.saldo)
nubank + 50 # Isso só é possivel por causa do metodo especial __add__ que foi criado na classe
print(nubank.saldo)


#__doc__
class Conta3(object):
    '''
    Objeto do Tipo Conta
    Estas string é exibida pelo metodo especial __doc__
    '''
    def __init__(self, idConta, saldo):
        '''
        Este comentario é exibido pelo metodo especial __doc__
        :param idConta:
        :param saldo:
        '''
        self.idConta = idConta
        self.saldo = saldo

itau = Conta3(987, 500)
print(itau.__doc__)
print(itau.__init__.__doc__)

#issubclass(subclasse, superclasse) - Verifica se a Subclasse passada é filha da SuperClasse
class Pai(object):
    pass
class Filha(Pai):
    pass
class Neta(Filha):
    pass

print(issubclass(Filha, Pai)) # Classe Filha é Subclasse da Pai
print(issubclass(Pai, Neta)) # Classe Pai não é subclasse da Neta
print(Filha.__bases__) # Outro metodo especial para verificar Super Classe


#callabe(objeto) - Retorna se o objeto pode ser invocado
print(callable(Pai))

class Conta4(object):
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def __call__(self, x): # Se criar o metodo __call__ na classe a mesma pode se torna callabe
        return x

bradesco = Conta4(394, 900)
print(bradesco('Esta string so foi retornada devido ao metodo __call__'))
=======
#__str__
class Conta(object):
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def __str__(self): #Esse metodo especial transforma a classe em uma string
        return f'ID: {self.idConta}\nSaldo: R${self.saldo}'

viacredi = Conta(123, 5000)
print(viacredi)

#__add__
class Conta2(object):
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def __add__(self, valor):
        self.saldo += valor

nubank = Conta2(456, 1000)
nubank.__add__(50)
print(nubank.saldo)
nubank + 50 # Isso só é possivel por causa do metodo especial __add__ que foi criado na classe
print(nubank.saldo)


#__doc__
class Conta3(object):
    '''
    Objeto do Tipo Conta
    Estas string é exibida pelo metodo especial __doc__
    '''
    def __init__(self, idConta, saldo):
        '''
        Este comentario é exibido pelo metodo especial __doc__
        :param idConta:
        :param saldo:
        '''
        self.idConta = idConta
        self.saldo = saldo

itau = Conta3(987, 500)
print(itau.__doc__)
print(itau.__init__.__doc__)

#issubclass(subclasse, superclasse) - Verifica se a Subclasse passada é filha da SuperClasse
class Pai(object):
    pass
class Filha(Pai):
    pass
class Neta(Filha):
    pass

print(issubclass(Filha, Pai)) # Classe Filha é Subclasse da Pai
print(issubclass(Pai, Neta)) # Classe Pai não é subclasse da Neta
print(Filha.__bases__) # Outro metodo especial para verificar Super Classe


#callabe(objeto) - Retorna se o objeto pode ser invocado
print(callable(Pai))

class Conta4(object):
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def __call__(self, x): # Se criar o metodo __call__ na classe a mesma pode se torna callabe
        return x

bradesco = Conta4(394, 900)
print(bradesco('Esta string so foi retornada devido ao metodo __call__'))
>>>>>>> Stashed changes
