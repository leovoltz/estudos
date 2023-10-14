tabuada = 1
while tabuada < 10:
    multiplicador = 1
    while multiplicador < 10:
        resultado = tabuada * multiplicador
        codigo = '{tabuada} * {multiplicador} = {resultado}'
        print(codigo.format(tabuada=tabuada, multiplicador=multiplicador, resultado= resultado))
        multiplicador += 1
    tabuada += 1
    print()