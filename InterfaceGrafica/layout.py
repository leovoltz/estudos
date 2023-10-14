# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão 1')
botao.setStyleSheet('font-size: 80px; color: white; font-family: sans serif')

botao2 = QPushButton('Texto do botão 2')
botao2.setStyleSheet('font-size: 40px; color: white; font-family: sans serif')

botao3 = QPushButton('Texto do botão 3')
botao3.setStyleSheet('font-size: 40px; color: white; font-family: sans serif')

main_widget = QWidget()

layout = QGridLayout()
main_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

main_widget.show()  # Central widget entre na hierarquia e exiba a janela.
app.exec()
