<<<<<<< Updated upstream
class Retangulo(object):
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    def mudaLado(self, ladoMudar, novoLado):
        if ladoMudar == 1:
            self.ladoA = novoLado
        elif ladoMudar == 2:
            self.ladoB = novoLado
    def retornLado(self, ladoVerif):
        if ladoVerif == 1:
            return self.ladoA
        elif ladoVerif == 2:
            return self.ladoB
    def calculaArea(self):
        #A = LadoA * LadoB
        return self.ladoA * self.ladoB
    def calculaPerimetro(self):
        #P = 2 *(LadoA + LadoB)
        return 2 * (self.ladoA + self.ladoB)

objeto = Retangulo(2, 4)

print(f'Area = {objeto.calculaArea()}')
print(f'Perimetro = {objeto.calculaPerimetro()}')

# Programa que utiliza o objeto

print('-=' * 25)
print('Informe a area de um Local para calcular quantos pisos serão utilizados ')
largura = float(input('Informe a Largura do Local em MT: '))
altura = float(input('Informe o Comprimento do Local em MT: '))

local = Retangulo(largura, altura)

print(f'O Local tem Area de {local.calculaArea()} mt')
print(f'O Local tem Perimetro de {local.calculaPerimetro()} mt')
=======
class Retangulo(object):
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    def mudaLado(self, ladoMudar, novoLado):
        if ladoMudar == 1:
            self.ladoA = novoLado
        elif ladoMudar == 2:
            self.ladoB = novoLado
    def retornLado(self, ladoVerif):
        if ladoVerif == 1:
            return self.ladoA
        elif ladoVerif == 2:
            return self.ladoB
    def calculaArea(self):
        #A = LadoA * LadoB
        return self.ladoA * self.ladoB
    def calculaPerimetro(self):
        #P = 2 *(LadoA + LadoB)
        return 2 * (self.ladoA + self.ladoB)

objeto = Retangulo(2, 4)

print(f'Area = {objeto.calculaArea()}')
print(f'Perimetro = {objeto.calculaPerimetro()}')

# Programa que utiliza o objeto

print('-=' * 25)
print('Informe a area de um Local para calcular quantos pisos serão utilizados ')
largura = float(input('Informe a Largura do Local em MT: '))
altura = float(input('Informe o Comprimento do Local em MT: '))

local = Retangulo(largura, altura)

print(f'O Local tem Area de {local.calculaArea()} mt')
print(f'O Local tem Perimetro de {local.calculaPerimetro()} mt')
>>>>>>> Stashed changes
