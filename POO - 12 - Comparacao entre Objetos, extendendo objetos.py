class Conta(object):
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor


itau = Conta(123, 4000) # Inicializa instancia de objeto referenciando a classe
bradesco = Conta(123, 5000)

print(itau == bradesco) # Compara um objeto a outro
print(id(itau)) # Mostra o endereço de memoria da variavel




'''Metodos de comparação de objetos
__le__ x <= y
__eq__ x == y
__ge__ x >= y
__lt__ x < y
__gt__ x > y
__ne__ x != y
'''


class Conta2(object):
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
    def __le__(self, other):
        if self.idConta <= other.idConta:
            return True
        return False
    def __eq__(self, other):
        if self.idConta == other.idConta:
            return True
        return False
    def __ge__(self, other):
        if self.idConta >= other.idConta:
            return True
        return False
    def __lt__(self, other):
        if self.idConta < other.idConta:
            return True
        return False
    def __gt__(self, other):
        if self.idConta > other.idConta:
            return True
        return False
    def __ne__(self, other):
        if self.idConta != other.idConta:
            return True
        return False

# Cria instancia de objeto para fazer a comparação
itau2 = Conta2(123, 5000)
bradesco2 = Conta2(456, 4000)
viacredi = Conta2(789, 1000)
caixa = Conta2(123, 500)

print(itau2 == caixa)
print(caixa == itau2)
print(bradesco2 > viacredi)

class Conta(object):
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor


itau = Conta(123, 4000) # Inicializa instancia de objeto referenciando a classe
bradesco = Conta(123, 5000)

print(itau == bradesco) # Compara um objeto a outro
print(id(itau)) # Mostra o endereço de memoria da variavel




'''Metodos de comparação de objetos
__le__ x <= y
__eq__ x == y
__ge__ x >= y
__lt__ x < y
__gt__ x > y
__ne__ x != y
'''


class Conta2(object):
    def __init__(self, idConta, saldo):
        self.idConta = idConta
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
    def __le__(self, other):
        if self.idConta <= other.idConta:
            return True
        return False
    def __eq__(self, other):
        if self.idConta == other.idConta:
            return True
        return False
    def __ge__(self, other):
        if self.idConta >= other.idConta:
            return True
        return False
    def __lt__(self, other):
        if self.idConta < other.idConta:
            return True
        return False
    def __gt__(self, other):
        if self.idConta > other.idConta:
            return True
        return False
    def __ne__(self, other):
        if self.idConta != other.idConta:
            return True
        return False

# Cria instancia de objeto para fazer a comparação
itau2 = Conta2(123, 5000)
bradesco2 = Conta2(500, 4250)
viacredi = Conta2(699, 1200)
caixa = Conta2(124, 520)

print(itau2 == caixa)
print(caixa == itau2)
print(bradesco2 > viacredi)
