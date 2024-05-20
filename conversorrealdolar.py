brl = float(input('Digite quanto você tem: R$'))
dolar = brl / 5.14
euro = brl / 5.56
iene = brl * 30.33
print('R${} \nUS${:.2f} DOLARES \n€{:.2f} EUROS \n¥{:.2f} IENE'
    .format(brl, dolar, euro, iene))
