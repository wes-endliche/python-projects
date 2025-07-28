numero = int(input('Digite um número inteiro: '))
lista_primos = []

for i in range(2, numero):
    #É primo até que se prove ao contrário
    primo = True
    
    #Testa se o número é divisível por mais números
    for teste in range(2, i):
        if i % teste == 0:
            primo = False
            break
    
    #Adiciona os números que passaram no teste
    if primo:
        lista_primos.append(i)

print(f'Lista de números primos: {lista_primos}')