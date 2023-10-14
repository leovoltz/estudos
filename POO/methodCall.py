
# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome, *args, **kwargs):
        print(f'{nome} está chamando o telefone: {self.phone}')
        return 1312

call1 = CallMe('54 98724-5565')
retorno = call1('Jorge Lucas')
print(retorno)