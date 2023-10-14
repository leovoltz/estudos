# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa():
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anônimo', idade)


p1 = Pessoa('João', 16)
p2 = Pessoa.criar_com_50_anos('Maria')
p3 = Pessoa.criar_anonimo('20')
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
# Pessoa.metodo_de_classe(p1)