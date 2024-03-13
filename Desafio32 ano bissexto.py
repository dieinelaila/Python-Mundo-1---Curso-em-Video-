from datetime import date
ano = int (input('Que ano quer analisar? Digite 0 para data atual : '))
if ano ==0:
    ano = date.today().year
if (4 != 0 or 100 == 0) and 400 != 0:
    print('O ano {} não é Bissexto'.format(ano))
else:
    print( 'O ano {} é Bissexto'.format(ano))

