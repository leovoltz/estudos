#Métodos em instâncias de classe Python
class Carro:
    def __init__(self, nome='Sei lá'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fox = Carro('Fox')
print(fox.nome)
fox.acelerar()

i30 = Carro(nome='i30')
print(i30.nome)
i30.acelerar()

