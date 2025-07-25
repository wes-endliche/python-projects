'''Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

O valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.'''

preco_diesel = 2
preco_etanol = 1.7

litros = int(input('Quantos litros de combustivel gostaria de adquirir? '))
combustivel = input('Diesel ou etanol? ').lower()

if combustivel == 'etanol' and litros <= 15:
    valor_total = preco_etanol * litros
    desconto = valor_total * 0.02
    valor_final = valor_total - desconto
    print('O valor a ser pago é R$%.2f.' %(valor_final))
elif combustivel == 'etanol' and litros > 15:
    valor_total = preco_etanol * litros
    desconto = valor_total * 0.04
    valor_final = valor_total - desconto
    print('O valor a ser pago é R$%.2f.' %(valor_final))
elif combustivel == 'diesel' and litros <= 15:
    valor_total = preco_diesel * litros
    desconto = valor_total * 0.03
    valor_final = valor_total - desconto
    print('O valor a ser pago é R$%.2f.' %(valor_final))
elif combustivel == 'diesel' and litros > 15:
    valor_total = preco_diesel * litros
    desconto = valor_total * 0.05
    valor_final = valor_total - desconto
    print('O valor a ser pago é R$%.2f.' %(valor_final))
else:
    print('Entrada inválida. Tente novamente.')