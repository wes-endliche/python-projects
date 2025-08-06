atividade_1 = int(input('Quanto tempo irá levar para concluir a primeira atividade? '))
atividade_2 = int(input('E a segunda atividade? '))
atividade_3 = int(input('E a terceira? '))

if atividade_1 < 0 or atividade_2 < 0 or atividade_3 < 0:
    print('Erro: Os dias não podem ser negativos.')
else:
    total_dias = atividade_1 + atividade_2 + atividade_3
    print(f'Irá levar {total_dias} dias para concluir o projeto.')