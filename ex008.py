#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2m

l = float(input('digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
a2 = l * a
a3 = a2 / 2

print('=' * 12)
print(f'A quantidade de latas de tintas usadas para pintar a parede é {a3:.2f})
print('=' * 12)
