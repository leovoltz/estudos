# Atributos de classe

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 200

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('João', 35)
p2 = Pessoa('Carla', 15)

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
