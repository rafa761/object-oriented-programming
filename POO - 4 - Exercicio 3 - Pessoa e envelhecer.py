<<<<<<< Updated upstream
class Pessoa(object):
    def __init__(self):
        self.nome = 'Rafael'
        self.idade = 15
        self.peso = 67.00
        self.altura = 1.65
    def envelhecer(self, anosEnvelhecer):
        if self.idade < 20:
            self.altura += anosEnvelhecer * 0.5
    def engordar(self, pesoAdicionar):
        self.peso += pesoAdicionar
    def emagrecer(self, pesoSubtrair):
        self.peso -= pesoSubtrair
    def crescer(self, alturaAdd):
        self.altura += alturaAdd
    def retornaPessoa(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}Kg')
        print(f'Altura: {self.altura}')

objeto = Pessoa()

objeto.retornaPessoa()
print()
objeto.emagrecer(2)
objeto.crescer(0.08)
objeto.engordar(5)
objeto.retornaPessoa()
=======
class Pessoa(object):
    def __init__(self):
        self.nome = 'Rafael'
        self.idade = 15
        self.peso = 67.00
        self.altura = 1.65
    def envelhecer(self, anosEnvelhecer):
        if self.idade < 20:
            self.altura += anosEnvelhecer * 0.5
    def engordar(self, pesoAdicionar):
        self.peso += pesoAdicionar
    def emagrecer(self, pesoSubtrair):
        self.peso -= pesoSubtrair
    def crescer(self, alturaAdd):
        self.altura += alturaAdd
    def retornaPessoa(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}Kg')
        print(f'Altura: {self.altura}')

objeto = Pessoa()

objeto.retornaPessoa()
print()
objeto.emagrecer(2)
objeto.crescer(0.08)
objeto.engordar(5)
objeto.retornaPessoa()
>>>>>>> Stashed changes
