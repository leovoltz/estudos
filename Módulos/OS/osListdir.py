# os,listdir para navegar em caminhos.
# /home/tesudin/Downloads/IA Images/'
import os
caminho = os.path.join('/home', 'tesudin', 'Downloads', 'IA Images')

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)

    if not os.path.isdir(caminho_completo):
        continue

    for imagem in os.listdir(caminho_completo):
        print(imagem)
