renda = float(input('Digite sua renda mensal atual: R$'))
limite = renda*0.3 #limite de 30% 
emprestimo = float(input('Quanto deseja pegar emprestado? (R$1000.00 - R$20000.00) R$'))
parcelas = int(input('Em quantas vezes deseja parcelar? (2 - 12)'))
valor_parcela = (emprestimo * 1.15)/parcelas #15% de taxa de juros


if renda <= 2000 or valor_parcela > limite:
    print(f'Empréstimo negado! As parcelas ficaram R${valor_parcela}, e o seu limite é de R${limite}.')
else:
    print(f'Empréstimo confirmado! Para o seu empréstimo de R${emprestimo}, você pagará R${valor_parcela} em {parcelas}x.')