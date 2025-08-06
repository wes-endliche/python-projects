temperatura = int(input('Digite a temperatura atual: '))

if temperatura > 25:
    print('Alerta! Temperatura acima do limite permitido.')
elif temperatura < 16:
    print('Temperatura menor do que o ar condicionado consegue atingir.')
else:
    print('Temperatura definida!')