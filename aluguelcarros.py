km = int(input('Quantidade de km percorrido: '))
diasAlugados = float(input('Quantidade de dias alugados: '))
preçoDia = (diasAlugados * 60) + (diasAlugados * 0.15)
print('O total a pagar é de R${:.2f}'.format(preçoDia))