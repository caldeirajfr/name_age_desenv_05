def idade():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    while True:
        if (ano_nascimento > 1922 and ano_nascimento < 2021):
            idade = 2022 - ano_nascimento
            print("Sua idade é: " + str(idade))
            break
        else:
            print("Ano inválido")
            ano_nascimento = int(input("Digite o ano de nascimento válido: "))
            
idade()