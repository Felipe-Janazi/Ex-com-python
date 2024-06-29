print("************************************")
print("* Bem vindo ao jogo de adivinhação *")
print("************************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

print("Você digitou: ", chute_str)

""" Necessário mudar o valor da variavel pois ela vem como string e não 
se pode fazer comparação de uma string com uma num pois sempre dará false """

chute = int(chute_str)

""" SIGNIFICA QUE SE A VARIAVEL ABAIXO FOR VERDADEIRA ENTÃO IRÁ EXECUTAR O IF"""
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou")
else:
    if(maior):
        print("Você errou! O seu chute foi maior do que o número secreto")

        """ A ELIF É BASICAMENTE A MESMA COISA QUE UM ELSE IF EM JS, ALÉM DE QUE O ELSE 
        NÃO ACEITA CONDIÇÕES, ENTÃO PARA ISSO TEMOS QUE USAR O ELIF"""
    elif(menor):
        print("Você errou! O seu chute foi menor do que o número secreto")

print("Fim do jogo!")