# import math
# num = float(input('Digite um valor: '))
# print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, math.trunc(num)))

from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))
