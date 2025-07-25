idade = int(input('Informe a idade (ou um número negativo para encerrar): '))

contador_0_25 = 0 
contador_26_50 = 0 
contador_51_75 = 0 
contador_76_100 = 0 

while idade >= 0:
    if idade >= 0 and idade <= 25:
        contador_0_25 += 1
    elif idade >= 26 and idade <= 50:
        contador_26_50 += 1
    elif idade >= 51 and idade <= 75:
        contador_51_75 += 1
    elif idade >= 76 and idade <= 100:
        contador_76_100 += 1
     
    idade = int(input('Informe a idade (ou um número negativo para encerrar): '))

print('Distribuição de idades:')
print('[0-25]:', contador_0_25)
print('[26-50]:', contador_26_50)
print('[51-75]:', contador_51_75)
print('[76-100]:', contador_76_100)