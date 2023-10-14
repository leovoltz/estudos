def multiplicar(*args):
    total = 1
    for n in args:
        total *= n
        print(n)
    return total


multi = multiplicar(1,2,3,4,5)
print(multi)

# ----------------------------------------------------------------------------------

def impar_par(number:int):
    multiplo_de_dois = number % 2 == 0
    if multiplo_de_dois:
        return f"O número {number} é par"
    return f"O número {number} é ímpar"


print(impar_par(111))