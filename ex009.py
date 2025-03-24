#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Digite o valor do produto desejado R$: '))
p2 =(p * 5) / 100
p3 = p - p2

print('=' * 12)
print(f'O valor do produto com desconto será {p3}')
print('=' * 12)
