# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

caminho = os.path.join('Destkop', 'Curso', 'Arquivo.txt')
# print(caminho)
diretorio, arquivo = os.path.split(caminho)
# Separar caminho e extensão:
nome_arquivo, extensao_arquivo = os.path.splitext(caminho)
# Printar e exibir as informações separadas:
print(nome_arquivo, extensao_arquivo)
# Verificar se algum caminho exist:
print(os.path.exists(caminho))
# Trazer o caminho atual onde você está no momento.
print(os.path.abspath('.'))
# Trás a parte final do seu caminho:
print(os.path.basename(caminho))
# Ele trás o dirname e separada do final/arquivo.
print(os.path.dirname(caminho))
