# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - FAça a ligação entre Carro tem Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça uma ligação entre Carro e Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela.

class Carro:
    
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    
    def __init__(self, nome) -> None:
        self.nome = nome

class Fabricante:
    
    def __init__(self, nome) -> None:
        self.nome = nome


fox = Carro('Fox')
motor1_6 = Motor(1.6)
volkswagen = Fabricante('Volkswagen')
fox.motor = motor1_6.nome
fox. fabricante = volkswagen.nome

virtus = Carro('Virtus')
virtus.motor = motor1_6.nome
virtus.fabricante = volkswagen.nome

i30 = Carro('i30')
hyundai = Fabricante('Hyunday')
motor1_8 = Motor(1.8)
i30.motor = motor1_8.nome
i30.fabricante = hyundai.nome

print(f'Modelo: {fox.nome} - Motor: {fox.motor} - Fabricante: {fox.fabricante}')
print(f'Modelo: {i30.nome} - Motor: {i30.motor} - Fabricante: {i30.fabricante}')
print(f'Modelo: {virtus.nome} - Motor: {virtus.motor} - Fabricante: {virtus.fabricante}')

