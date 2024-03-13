real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 4.95
euro = real / 5.37

print('Com R$ {:.2f} você pode comprar \nUS$ {:.2f} \nEuro {:.2f}. '.format(real,dolar,euro))
