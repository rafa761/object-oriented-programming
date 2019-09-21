<<<<<<< Updated upstream
#Classe
class Mamifero(object):
    def __init__(self, corPelo, genero, numPatas):
        self.corPelo = corPelo
        self.genero = genero
        self.numPatas = numPatas
    def falar(self):
        print('Olá sou um Mamifero e eu sei falar')
    def andar(self):
        print(f'Estou andando sobre {self.numPatas} patas')
    def amamentar(self):
        if self.genero.upper()[0] == 'M':
            print('Machos nao amamentam')
            return
        print('Amamentando Filhote')

#Objeto recebe classe. Ele é uma instancia da classe
maffu = Mamifero('amarela', 'f', 4)
maffu.amamentar()
maffu.andar()

andressa = Mamifero('preto', 'f', 2)

#Cria uma subClasse, indicando a classe Mamifero como Super Classe
class Pessoa(Mamifero):
    def __init__(self, corPelo, genero, numPatas, corCabelo):
        super(Pessoa, self).__init__(corPelo, genero, numPatas)
        self.corCabelo = corCabelo
    def falarSub(self):
        print(f'Olá eu sou uma pessoa e sei falar')
    def falarSuper(self):
        super(Pessoa, self).falar()

andressa = Pessoa('preto','f',2, 'castanho')
andressa.falarSub()
andressa.falarSuper()
=======
#Classe
class Mamifero(object):
    def __init__(self, corPelo, genero, numPatas):
        self.corPelo = corPelo
        self.genero = genero
        self.numPatas = numPatas
    def falar(self):
        print('Olá sou um Mamifero e eu sei falar')
    def andar(self):
        print(f'Estou andando sobre {self.numPatas} patas')
    def amamentar(self):
        if self.genero.upper()[0] == 'M':
            print('Machos nao amamentam')
            return
        print('Amamentando Filhote')

#Objeto recebe classe. Ele é uma instancia da classe
maffu = Mamifero('amarela', 'f', 4)
maffu.amamentar()
maffu.andar()

andressa = Mamifero('preto', 'f', 2)

#Cria uma subClasse, indicando a classe Mamifero como Super Classe
class Pessoa(Mamifero):
    def __init__(self, corPelo, genero, numPatas, corCabelo):
        super(Pessoa, self).__init__(corPelo, genero, numPatas)
        self.corCabelo = corCabelo
    def falarSub(self):
        print(f'Olá eu sou uma pessoa e sei falar')
    def falarSuper(self):
        super(Pessoa, self).falar()

andressa = Pessoa('preto','f',2, 'castanho')
andressa.falarSub()
andressa.falarSuper()
>>>>>>> Stashed changes
