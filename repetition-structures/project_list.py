projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:  # == None não é recomendado
        print('Projeto ausente')
        continue
    
    print(projeto)