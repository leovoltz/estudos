# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os,json

def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa para ser listada!")
        return
    for num, tarefa in enumerate(tarefas):
        print(f'{num} - Tarefa: {tarefa}')


def desfazer(tarefas, desfazer_tarefas):
    if not tarefas:
        print("Nenhuma tarefa para desfazer!")
        return
    tarefa = tarefas.pop()
    desfazer_tarefas.append(tarefa)
    listar(tarefas)


def refazer(tarefas, refazer_tarefas):
    if not refazer_tarefas:
        print('Nenhuma tarefa para refazer!')
        return
    refaz = faz_refaz_tarefas.pop()
    refazer_tarefas.append(refaz)
    tarefa = refazer_tarefas.pop()
    tarefas.append(tarefa)
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa!')
        return
    print(f'{tarefa=} adicionada a lista de tarefas')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def ler(tarefas, caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe!')
        salvar(tarefas, caminho)
    return dados
    
def salvar(tarefas, caminho):
    dados = tarefas
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'arquivo12.json'
tarefas = ler([], CAMINHO_ARQUIVO)
faz_refaz_tarefas = []

while True:
    print('~' * 50)
    print('\tDigite um comando ou tarefa:')
    print('Comandos: Listar, Desfazer e Refazer')
    print('~' * 50)
    print()
    escolha = input('').lower()

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, faz_refaz_tarefas),
        'refazer': lambda: refazer(tarefas, faz_refaz_tarefas),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(escolha, tarefas)
    }
    comando = comandos.get(escolha) if comandos.get(escolha) is not None \
    else comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)