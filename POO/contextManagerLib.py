# Contex Manager com função - Criando e Usando gerenciadores de contexto.

from contextlib import contextmanager


@contextmanager
def my_open(file_path, mode):
    try:
        print('Opening file...')
        file = open(file_path, mode, encoding='utf8')
        yield file
    finally:
        print('Closing file...')
        file.close()


with my_open('aula150.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    print('WITH', file)
