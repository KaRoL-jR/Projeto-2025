#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

s = float(input('Quanto você recebe mensalmente? '))
p = (s * 15) / 100
r = p + s

print('=' * 12)
print(f'Seu novo salário é {r}')
print('=' * 12)
