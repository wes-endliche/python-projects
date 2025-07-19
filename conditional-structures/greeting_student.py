turno_de_estudo = input('Digite em qual turno você estuda: ')
turno_de_estudo = turno_de_estudo.lower()

if turno_de_estudo == 'manhã':
  print('Bom Dia!')
elif turno_de_estudo == 'tarde':
  print('Boa Tarde!')
elif turno_de_estudo == 'noite':
  print('Boa Noite!')
else:
  print('Valor Inválido!')