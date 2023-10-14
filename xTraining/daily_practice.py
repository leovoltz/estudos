import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

fmt = '%Y-%m-%d'
data_meta = datetime.strptime('2024-04-15', fmt)
delta = relativedelta(months=2)
data_max = data_meta + delta
calendario = calendar.month(2024, data_meta.month)
print(calendario)
print(f' Data planejada: {data_meta}\n'
      f' Data máxima: {data_max}')
primeiro_ultimo_dia_mes = calendar.monthrange(2024, 6)
print(calendar.day_name[primeiro_ultimo_dia_mes[0]])
