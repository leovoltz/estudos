# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'capitalize'

if hasattr(string, metodo):
    print('Existe', metodo)
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)


help(getattr)
