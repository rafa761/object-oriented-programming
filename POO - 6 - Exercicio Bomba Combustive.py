'''Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.'''
class BombaCombustivel(object):
    def __init__(self):
        self.tipoCombustivel = 'gasolina' # Tipo Combustivel
        self.valLitro = 4.40 # Valor por Litro
        self.qtdCombustivel = 100 # qtd Litros na Bomba
    def abastValor(self, valorAbast):
        ltAbastecido = valorAbast / self.valLitro
        self.qtdCombustivel -= ltAbastecido
        return print(f'Foram abastecidos {ltAbastecido:.2f} Litros de {self.tipoCombustivel}')
    def abastLitro(self, ltAbast):
        valAbastecido = ltAbast * self.valLitro
        self.qtdCombustivel -= ltAbast
        return print(f'Valor a ser pago é R${valAbastecido:.2f}')
    def alteraValorComb(self, novoValor):
        self.valLitro = novoValor
    def alteraTipoComb(self, novoTipo):
        self.tipoCombustivel = novoTipo
    def alteraQtdComb(self, novaQtdComb):
        self.tipoCombustivel = novaQtdComb
    def verificaBomba(self):
        print(f'A Bomba tem combustivel {self.tipoCombustivel}')
        print(f'O Valor por LT é R${self.valLitro}')
        print(f'Resta {self.qtdCombustivel:.1f} LT na bomba')

bomba = BombaCombustivel()
bomba.verificaBomba()
bomba.abastLitro(10)
bomba.verificaBomba()
