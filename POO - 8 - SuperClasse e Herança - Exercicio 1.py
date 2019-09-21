<<<<<<< Updated upstream
class ObjetoGrafico(object):
    def __init__(self, cor = 'branco', preenchida = True, contorno = 1):
        self.corPreenchimento = cor
        self.preenchida = bool(preenchida)
        self.contorno = contorno

class Retangulo(ObjetoGrafico):
    def __init__(self, cor, preenchida, contorno, base, altura):
        super(Retangulo, self).__init__(cor, preenchida, contorno)
        self.base = base
        self.altura = altura

objetoGraph = ObjetoGrafico('Azul', True, 2) #Criando instancia(Objeto) da Classe
objRetang = Retangulo('Verde', True, 2, 4, 6)
print(objRetang.corPreenchimento) #Acessando Atributo da Super Classe


class Circulo(ObjetoGrafico):
    def __init__(self, cor, preenchida, contorno, raio):
        super(Circulo, self).__init__(cor, preenchida, contorno)
        self.raio = raio

objCirculo = Circulo('vermelho', True, 4, 20)
print(objCirculo.contorno) #Acessa Atributo da Super Classe
print(objCirculo.raio) #Acessa Atributo da Sub Classe

class Triangulo(ObjetoGrafico):
    def __init__(self, cor, preenchida, contorno, base, altura):
        super(Triangulo, self).__init__(cor, preenchida, contorno)
        self.base = base
        self.altura = altura

objTriang = Triangulo('amarelo', False, 6, 8, 10)
print(objTriang.preenchida) # Acessa Atributo Super Classe
=======
class ObjetoGrafico(object):
    def __init__(self, cor = 'branco', preenchida = True, contorno = 1):
        self.corPreenchimento = cor
        self.preenchida = bool(preenchida)
        self.contorno = contorno

class Retangulo(ObjetoGrafico):
    def __init__(self, cor, preenchida, contorno, base, altura):
        super(Retangulo, self).__init__(cor, preenchida, contorno)
        self.base = base
        self.altura = altura

objetoGraph = ObjetoGrafico('Azul', True, 2) #Criando instancia(Objeto) da Classe
objRetang = Retangulo('Verde', True, 2, 4, 6)
print(objRetang.corPreenchimento) #Acessando Atributo da Super Classe


class Circulo(ObjetoGrafico):
    def __init__(self, cor, preenchida, contorno, raio):
        super(Circulo, self).__init__(cor, preenchida, contorno)
        self.raio = raio

objCirculo = Circulo('vermelho', True, 4, 20)
print(objCirculo.contorno) #Acessa Atributo da Super Classe
print(objCirculo.raio) #Acessa Atributo da Sub Classe

class Triangulo(ObjetoGrafico):
    def __init__(self, cor, preenchida, contorno, base, altura):
        super(Triangulo, self).__init__(cor, preenchida, contorno)
        self.base = base
        self.altura = altura

objTriang = Triangulo('amarelo', False, 6, 8, 10)
print(objTriang.preenchida) # Acessa Atributo Super Classe
>>>>>>> Stashed changes
