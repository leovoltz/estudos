# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
cliente1.append('Carlos')
print(cliente1)
 
cliente2 = adiciona_clientes('Jorge')
adiciona_clientes('Marcela', cliente2)
print(cliente2)