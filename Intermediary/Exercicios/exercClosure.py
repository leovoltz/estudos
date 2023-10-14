
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
print(duplicar(10))

triplicar = criar_multiplicador(3)
print(triplicar(3))

