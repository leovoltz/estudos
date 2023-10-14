import os
import calendar
from datetime import datetime

os.system('clear')
calendario = calendar.calendar(2023)
data_atual = datetime.now()
print(calendario)
print(data_atual.strftime('%D/%m/%Y - %H:%M:%S'))
home = os.path.expanduser('~')
arquivo = os.path.join(home, 'Área de trabalho', 'arquivo.txt')
firstday, lastday = calendar.monthrange(2023, 8)
day_one = calendar.day_name[firstday]
last_day = calendar.day_name[calendar.weekday(2023, 8, lastday)]
print(day_one)
print(last_day)

with open(arquivo, 'w') as file:
    file.write(calendario)
