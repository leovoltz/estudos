# __dict++ e vars ára atributos de instância.
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)
# p1.nome = 'Errei'
# print(p1.nome)

# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'Errei'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
print(vars(p1))
print(p1.nome)