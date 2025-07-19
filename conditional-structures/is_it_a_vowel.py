letra = input('Digite uma letra: ').lower()
vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvwxyz'

if letra in vogais:
    print('A letra é uma vogal.')
elif letra in consoantes:
    print('A letra é uma consoante.')
else:
    print('Entrada inválida. Por favor, digite uma letra válida.')
