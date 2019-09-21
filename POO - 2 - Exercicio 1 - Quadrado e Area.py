<<<<<<< Updated upstream
#Definicao da Classe
class Quadrado(object):
    def __init__(self, lado1 = 0, lado2 = 0):
        self.lado1 = lado1
        self.lado2 = lado2
        print('Construtor chamado')
    def alteraLado(self, lado, novoValor):
        if lado == 1:
            self.lado1 = novoValor
        elif lado == 2:
            self.lado2 = novoValor
    def retornaLado(self, lado):
        if lado == 1:
            return self.lado1
        elif lado == 2:
            return self.lado2
    def calcArea(self):
        return self.lado1 * self.lado2


#Chamando a classe a atribuindo a um objeto
quadrado = Quadrado(2, 2)

print(quadrado.retornaLado(1))
print(quadrado.alteraLado(2, 6))
print(quadrado.calcArea())
=======
#Definicao da Classe
class Quadrado(object):
    def __init__(self, lado1 = 0, lado2 = 0):
        self.lado1 = lado1
        self.lado2 = lado2
        print('Construtor chamado')
    def alteraLado(self, lado, novoValor):
        if lado == 1:
            self.lado1 = novoValor
        elif lado == 2:
            self.lado2 = novoValor
    def retornaLado(self, lado):
        if lado == 1:
            return self.lado1
        elif lado == 2:
            return self.lado2
    def calcArea(self):
        return self.lado1 * self.lado2


#Chamando a classe a atribuindo a um objeto
quadrado = Quadrado(2, 2)

print(quadrado.retornaLado(1))
print(quadrado.alteraLado(2, 6))
print(quadrado.calcArea())
>>>>>>> Stashed changes
