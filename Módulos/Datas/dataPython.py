# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

data_str_data = '2023-07-23 14:19:50'
data_str_data = '23/07/2023'
data_str_formato = '%d/%m/%Y'
# data_str_formato = '%Y-%m-%d %H:%M:%S'

# data = datetime(2023, 7, 23, 14, 29, 50)
data = datetime.strptime(data_str_data, data_str_formato)
print(data)

# -----------------------------------------
# Timezone - Fuso horário do relógio/data
data = datetime.now(timezone('Asia/Tokyo'))
# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))

print(data)

# ------------------------------------------
# Data Stamp - Segundos desde 1970 até a data de hoje
data = datetime.now()
print(data.timestamp())  # Isso está na base de dados.
# Número que vai ser lido e formar a data.
print(datetime.fromtimestamp(1690134902))
