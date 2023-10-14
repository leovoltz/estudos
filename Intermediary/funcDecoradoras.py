# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def make_func(func):
    def internal(*args, **kwargs):
        print('Vou te decorar!')
        for arg in args:
            is_string(arg)

        result = func(*args, **kwargs)
        print(f'O seu resultado foi {result}')
        print('Ok, agora você foi decorada')
        return result
    return internal


def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param need to be an string')


inverte_string_checando_parametro = make_func(inverte_string)

invertida = inverte_string_checando_parametro('123')
print(invertida)
