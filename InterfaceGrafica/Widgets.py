# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
# https://doc.qt.io/qtforpython-6/quickstart.html
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px; color: red; font-family: sans serif')
botao.show()  # Adiciona o widget na hierarquia e exibe a janela.

app.exec()
