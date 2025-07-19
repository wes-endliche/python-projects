produto_1 = float(input('Quanto custa o primeiro produto? R$'))
produto_2 = float(input('Quanto custa o segundo produto? R$'))
produto_3 = float(input('Quanto custa o terceiro produto? R$'))
print(f'O preço dos produtos é R${produto_1}, R${produto_2} e R${produto_3}.')

if produto_1 < produto_2 and produto_1 < produto_3:
  print(f'O mais barato é R${produto_1}')
elif produto_2 < produto_1 and produto_2 < produto_3:
  print(f'O mais barato é R${produto_2}')
elif produto_3 < produto_1 and produto_3 < produto_2:
  print(f'O mais barato é R${produto_3}')