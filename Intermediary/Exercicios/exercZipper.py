# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
sigla = ['BA', 'SP', 'MG', 'RJ']
resultado = [uni for uni in list(zip_longest(cidade,sigla,fillvalue='Null'))]
print(resultado)