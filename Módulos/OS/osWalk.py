# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursida. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretóorio atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('/home', 'tesudin', 'Downloads', 'IA Images')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        print('  ', the_counter, 'File:', file_)
        # os.unlink(caminho_) - Comando para "deslinkar"/excluir files, etc...
