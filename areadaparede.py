larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tint = area / 2
print('Sua parede tem a dimensão de {}m x {}m, e a area é de {:.2f}m²'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta'.format(tint))