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


# def zipper(list1, list2):
#     intervalo = min(len(list1), len(list2))
#     return [
#         (list1[i], list2[i]) for i in range(intervalo)
#     ]

from itertools import zip_longest

city = ['Salvador', 'Ubatuba', 'Belo Horizonte']
state = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(city,state)))
print(list(zip_longest(city,state, fillvalue='No city')))


# resultado = (zipper(city,state))
# print(resultado)
