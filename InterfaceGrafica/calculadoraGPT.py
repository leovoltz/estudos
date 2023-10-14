import tkinter as tk

# Função para calcular o resultado


def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        resultado_label.config(text="Resultado: " + str(resultado))
    except Exception as e:
        print(e)
        resultado_label.config(text="Erro")


# Configuração da janela
janela = tk.Tk()
janela.title("Calculadora")

# Entrada de texto para a expressão
entrada = tk.Entry(janela, width=30)
entrada.grid(row=0, column=0, columnspan=4)

# Botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for texto in botoes:
    if texto == '=':
        botao = tk.Button(janela, text=texto, width=10, command=calcular)
    else:
        botao = tk.Button(janela, text=texto, width=10,
                          command=lambda t=texto: entrada.insert(tk.END, t))
    botao.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="Resultado: ")
resultado_label.grid(row=row_val, column=0, columnspan=4)

janela.mainloop()
