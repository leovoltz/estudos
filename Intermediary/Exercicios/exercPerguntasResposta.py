perguntas = [
    {
        'Pergunta': 'Quanto é 25 / 5?',
        'Opções': ['3', '5', '1', '15'],
        'Resposta': '5',
    },

    {
        'Pergunta': 'Linus Torvalds, é criador do?',
        'Opções': ['Windows', 'Linux', 'MAC', 'Unix'],
        'Resposta': 'Linux',
    },

    {
        'Pergunta': 'Em que ano se encerrou a 2º guerra mundial?',
        'Opções': ['1918', '1960', '2006', '1945'],
        'Resposta': '1945',
    },

    {
        'Pergunta': 'Qual é a capital do Brasil?',
        'Opções': ['Brasilia', 'Bahia', 'Buenos Aires', 'Rio de Janeiro'],
        'Resposta': 'Brasilia',
    },

    {
        'Pergunta': 'Quem ganhou a copa do mundo em 2022?',
        'Opções': ['França', 'Marrocos', 'Argentina', 'Brasil'],
        'Resposta': 'Argentina',
    },
]

acertos = 0
for pergunta in perguntas:
    print(f'Pergunta: {pergunta.get("Pergunta")}')
    print()
    opcoes = pergunta.get("Opções")
    for cod, opcao in enumerate(opcoes):
        print(f'({cod}) - {opcao}')
    
    try:
        escolha = int(input("Escolha uma das opções: "))
    except ValueError:
        print("Valor inválido, digite um das opções acima!")
        break
     
    qtd_opcoes = len(perguntas)

    if opcoes[escolha] == pergunta.get("Resposta"):
        acertos += 1
        print("Parabéns, você acertou!!")
        print()
    else:
        print("Eita, você errou! :/")
        print()

if acertos <3:
    print(f'Você acertou {acertos} de {qtd_opcoes}, mais sorte na próxima!')
else:
    print(f'Parabéns, você acertou {acertos} de {qtd_opcoes}!!')
    1
    