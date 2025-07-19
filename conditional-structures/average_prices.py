ano_um = float(input('Digite o valor médio do primeiro ano: R$'))
ano_dois = float(input('Digite o valor médio do segundo ano: R$'))
ano_tres = float(input('Digite o valor médio do terceiro ano: R$'))

if ano_um > ano_dois and ano_tres and ano_dois > ano_tres:
  print(f'O valor mais alto foi {ano_um}, e o mais baixo foi {ano_tres}')
elif ano_dois > ano_um and ano_tres and ano_um > ano_tres:
  print(f'O valor mais alto foi {ano_dois}, e o mais baixo foi {ano_tres}')
elif ano_tres > ano_um and ano_dois and ano_um > ano_dois:
  print(f'O valor mais alto foi {ano_tres}, e o mais baixo foi {ano_dois}')