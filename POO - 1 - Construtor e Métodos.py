<<<<<<< Updated upstream
class MeuObjeto(object): #Criação da Classe
    def __init__(self): # Constructor - constroi a classe
        self.nome = "Rafael" # Atributos do objeto
        self.idade = 27
        print('Construtor chamado com sucesso')
    def imprime(self): #Criação de um método do Objeto
        print(f'Ola meu nome é {self.nome} e tenho {self.idade}')


#Cria um objeto e atribui a classe
rafael = MeuObjeto()
print(rafael.imprime())


#Criando classe que recebe parametros
class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print('Construtor chamado com sucesso')
    def imprime(self, retorno):
        print(f'O {self.nome} tem {self.idade} anos')
        print(retorno)

individuo = Pessoa('maffu', 3)

print(individuo.imprime(5))
=======
class MeuObjeto(object): #Criação da Classe
    def __init__(self): # Constructor - constroi a classe
        self.nome = "Rafael" # Atributos do objeto
        self.idade = 27
        print('Construtor chamado com sucesso')
    def imprime(self): #Criação de um método do Objeto
        print(f'Ola meu nome é {self.nome} e tenho {self.idade}')


#Cria um objeto e atribui a classe
rafael = MeuObjeto()
print(rafael.imprime())


#Criando classe que recebe parametros
class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print('Construtor chamado com sucesso')
    def imprime(self, retorno):
        print(f'O {self.nome} tem {self.idade} anos')
        print(retorno)

individuo = Pessoa('maffu', 3)

print(individuo.imprime(5))
>>>>>>> Stashed changes
