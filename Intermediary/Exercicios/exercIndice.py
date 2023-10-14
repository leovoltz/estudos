# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('João')

# indices = range(len(lista))

# for indice in indices:
#     print(f'Indice: {indice} - Nome: {lista[indice]} Tipo: {type(lista[indice])}')


lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(f'Indice: {indice} - Nome: {nome } Tipo: {type(nome)}')