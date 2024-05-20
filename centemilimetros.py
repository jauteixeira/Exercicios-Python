n1 = float(input('DIGITE OS METROS: '))
cent = n1 * 100
mil = n1 * 1000
km = n1 / 1000
dec = n1 / 10
hec = n1 / 100
decim = n1 * 10
print('{} METROS EQUIVALE A \n{} CENTIMETROS, \n{} MILIMETROS, \n{} QUILOMETROS, \n{} DECAMETROS, \n{} HECTOMETROS, \n{} DECIMETROS'
    .format(n1, cent, mil, km, dec, hec, decim))
