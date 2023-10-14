# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
juros = 1.05
fmt = '%Y-%m-%d'
delta_anos = relativedelta(years=5)
inicio_empr = datetime.strptime('2020-12-20', fmt)
fim_empr = inicio_empr + delta_anos

data_parcelas = []
data_parcela = inicio_empr

while data_parcela < fim_empr:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

parcelas = len(data_parcelas)
valor_parcela = (valor_total / parcelas) * juros
total_pago = 0.0

while valor_parcela < valor_total:
    total_pago += valor_parcela
    if total_pago > valor_total:
        break

for num, data in enumerate(data_parcelas):
    print(data.strftime(
        f'Parcela:{num} Venc: %d/%m/%Y R$ {valor_parcela:,.2f}'))


print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
    f'O total pago será de: {total_pago:,.2f}'
)
