"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao=None, despedida=None):
    if saudacao is not None:
        def saudar(nome): 
            return f'{saudacao}, {nome}!'
        return saudar
    if despedida is not None:
        def despedir(nome):
            return f'{despedida}, {nome}!'
        return despedir


falar_bom_dia = criar_saudacao(saudacao='Bom dia')
despedida = criar_saudacao(despedida='Bom descanso')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(despedida(nome))