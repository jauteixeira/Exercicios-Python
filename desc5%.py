val = float(input('Digite o valor do produto: R$ '))
desc = val * 0.05
valfin = val - desc
print('O produto que custava {}, na promoção com 5% vai custar R${:.2f}'.format(val, valfin))
