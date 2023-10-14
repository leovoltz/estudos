# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# fmt = '%d/%m/%Y'
# data = datetime(2023, 7, 23, 16, 58, 45)
data = datetime.strptime('2023-07-23 16:58:45', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:S'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%d'), data.day)
print(data.strftime('%m'), data.month)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)
