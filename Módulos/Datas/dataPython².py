# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
# Timedelta é a diferença entre as datas.

from datetime import datetime  # timedelta

from dateutil.relativedelta import relativedelta


fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('01/01/2021 00:00:00', fmt)
data_fim = datetime.strptime('01/01/2024 00:00:00', fmt)
# delta = timedelta(days=10, hours=2)
delta = relativedelta(data_fim, data_inicio)
print(delta.days, delta.years)
print(data_fim - delta)
print(data_fim)
print(data_fim + relativedelta(seconds=60, minutes=10))

# delta = data_fim - data_inicio  # Diferença
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(data_fim > data_inicio)
