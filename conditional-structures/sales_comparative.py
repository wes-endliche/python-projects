banana = int(input('Digite a quantidade de bananas vendidas: '))
maca = int(input('Digite a quantidade de maçãs vendidas: '))

if banana > maca:
    print('As bananas tiveram mais vendas.')
elif banana == maca:
    print('Ambas as frutas tiveram o mesmo número de vendas.')
else:
    print('As maçãs tiveram mais vendas.')
