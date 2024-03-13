larg = float(input('Largura da parede: '))
alt = float (input('Altura da parede: '))
area = alt * larg
print('Sua parede tem a dimensao de {} e {} e sua área é de {} m2.'.format(larg, alt, area))

tinta = area/2
print('Para pintar essa parede, você precisará de {} litros de tinta.'.format(tinta))
