<<<<<<< Updated upstream
class Conta(object):
    totalBanco = 10000
    reserva = 0.10
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def deposito(self, valDeposito):
        self.saldo += valDeposito
        self.totalBanco += valDeposito
    def saque(self, valSaque):
        if self.saldo >= valSaque:
            self.saldo -= valSaque
            self.totalBanco -= valSaque


#Atributos com 2 underlines são encapsulados, ou seja, não podem ser acessados de fora da classe
class Conta(object):
    __totalBanco = 10000
    reserva = 0.10
    def __init__(self, idConta, saldo):
        self.__idConta = idConta
        self.saldo = saldo
    def deposito(self, valDeposito):
        self.saldo += valDeposito
        self.__totalBanco += valDeposito
    def saque(self, valSaque):
        if self.saldo >= valSaque:
            self.saldo -= valSaque
            self.totalBanco -= valSaque

viacredi = Conta(123, 5000)
viacredi.__totalBanco #Atributos com 2 underline não podem ser acessados
viacredi.__idConta
=======
class Conta(object):
    totalBanco = 10000
    reserva = 0.10
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def deposito(self, valDeposito):
        self.saldo += valDeposito
        self.totalBanco += valDeposito
    def saque(self, valSaque):
        if self.saldo >= valSaque:
            self.saldo -= valSaque
            self.totalBanco -= valSaque


#Atributos com 2 underlines são encapsulados, ou seja, não podem ser acessados de fora da classe
class Conta(object):
    __totalBanco = 10000
    reserva = 0.10
    def __init__(self, idConta, saldo):
        self.__idConta = idConta
        self.saldo = saldo
    def deposito(self, valDeposito):
        self.saldo += valDeposito
        self.__totalBanco += valDeposito
    def saque(self, valSaque):
        if self.saldo >= valSaque:
            self.saldo -= valSaque
            self.totalBanco -= valSaque

viacredi = Conta(123, 5000)
viacredi.__totalBanco #Atributos com 2 underline não podem ser acessados
viacredi.__idConta
>>>>>>> Stashed changes
