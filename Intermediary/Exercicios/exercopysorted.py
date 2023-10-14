# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from copy import deepcopy

from dados import produtos

novos_produtos = [{**item, 'preco':round(item['preco'] * 1.1, 2)} for item in deepcopy(produtos)]

print("Lista original:")
print(*produtos, sep= '\n')
print()

print("Lista com novos preços:")
print(*novos_produtos, sep= '\n')
print()

print("Lista ordenada por nome em ordem decrescente: ")
produtos_ordenados_por_nome = sorted(deepcopy(produtos), key= lambda i: i['nome'], reverse=True)
print(*produtos_ordenados_por_nome, sep='\n')
print()

print("Lista ordenada por preço em ordem crescente: ")
produtos_ordenados_por_preco = sorted(deepcopy(produtos), key= lambda i: i['preco'])
print(*produtos_ordenados_por_preco, sep= '\n')