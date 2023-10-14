from random import randint

for _ in range(100):

    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(randint(0, 9))

    contador_regressivo_1 = 10
    contador_regressivo_2 = 11

    resultado_1 = 0
    resultado_2 = 0
    for digito in nove_digitos:
        resultado_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos[:9] + str(digito_1)


    for digito in dez_digitos:
        resultado_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 10 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    form_cpf = cpf_gerado_pelo_calculo
    print(f'{form_cpf[0]}{form_cpf[1]}.{form_cpf[2]}{form_cpf[3]}{form_cpf[4]}.{form_cpf[5]}{form_cpf[6]}{form_cpf[7]}-{form_cpf[8]}{form_cpf[9]}')