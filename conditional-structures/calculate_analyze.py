#Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

valor_1 = int(input('Digite o primeiro número: '))
valor_2 = int(input('Digite o segundo número: '))
resultado_soma = valor_1 + valor_2
resultado_subtracao = valor_1 - valor_2
resultado_divisao = valor_1 / valor_2
resultado_multiplicacao = valor_1 * valor_2

print(f'Os valores escolhidos foram {valor_1} e {valor_2}')

operacao = input(f'O que deseja fazer com os dois números informados?\n  SOMAR | SUBTRAIR | DIVIDIR | MULTIPLICAR: ').upper()

def par_impar(null):
    if null % 2 == 0:
        print('Este valor é par.')
    else:
        print('Este valor é ímpar.')

def positivo_negativo(null):
    if null > 0:
        print('Este valor é positivo.')
    else:
        print('Este valor é negativo.')
        
def inteiro_decimal(null):
    if null % 1 == 0:
        print('O número é inteiro.')
    else:
        print('O número é decimal.')
       

if operacao == 'SOMAR':
    print(f'O resultado é {resultado_soma}')
    par_impar(resultado_soma)
    positivo_negativo(resultado_soma)
elif operacao == 'SUBTRAIR':
    print(f'O resultado é {resultado_subtracao}')
    par_impar(resultado_subtracao)
    positivo_negativo(resultado_subtracao)
elif operacao == 'DIVIDIR':
    print(f'O resultado é {resultado_divisao}')
    par_impar(resultado_divisao)
    positivo_negativo(resultado_divisao)
    inteiro_decimal(resultado_divisao)
elif operacao == 'MULTIPLICAR':
    print(f'O resultado é {resultado_multiplicacao}')
    par_impar(resultado_multiplicacao)
    positivo_negativo(resultado_multiplicacao)
else:
    print('Operação inválida. Digite novamente.')

