# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açucar sintático)

def make_func(func):
    def internal(*args, **kwargs):
        print('Vou te decorar!')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        result += ' Invertido'
        print(f'O seu resultado foi {result}')
        print('Ok, agora você foi decorada')
        return result
    return internal


@make_func
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param need to be an string')


invertida = inverte_string('123')
print(invertida)
