num = int(input('Digite um número de 1 a 10: '))

for i in range(1,11):
  if num > 10 or num < 1:
    num = int(input('Número inválido. Digite um número de 1 a 10: '))
  else:
    print(f'{num} x {i} = {num*i}')