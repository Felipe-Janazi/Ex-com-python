print("************************************")
print("* Bem vindo ao jogo de adivinhação *")
print("************************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

print("Você digitou: ", chute_str)

""" Necessário mudar o valor da variavel pois ela vem como string e não 
se pode fazer comparação de uma string com uma num pois sempre dará false """

chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")

print("Fim do jogo!")
