#Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm.

medida = float(input('Escolha um número para ser convertido em centímetros e milimetros: '))
cm = medida * 100
mm = medida * 1000

print('=' * 12)
print(f'Medida em centímetros é: {cm}')
print(f'Medida em milímetros fica: {mm}')
print('=' * 12)
