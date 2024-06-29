# Necessário importar o random para conseguir o utilizar em PY
import random

print("************************************")
print("* Bem vindo ao jogo de adivinhação *")
print("************************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print ("Qual o nível da dificuldade?")
print ("[1] Fácil  [2] Médio  [3] Difícil")
nivel = int(input ("Defina o nível: "))

if (nivel == 1): 
    total_de_tentativas = 20

if (nivel == 2):
    total_de_tentativas = 10

if (nivel == 3):
    total_de_tentativas = 5

# MANEIRA DE USAR O FOR, COLOCANDO A VARIAVEIL QUE SE INICIA E ATÉ ONDE ELA VAI, NESTE CASO ELA VAI IR DO 1 ATÉ O TOTAL DE TENTATIVAS, MAS O TOTAL DE TENTATIVAS VAI ATÉ UM ANTES, POR ISSO ADICIONAMOS MAIS UM PARA AGORA ELA IR ATÉ A TRÊS
# A POSIÇÃO FINAL É NÃO INCLUSIVA, ASSIM NECESSITANDO DE UM +1

# for rodada in range (1, 11, 3):
#     ESTA É UMA FORMA DE COLCOAR O INICIO (1) O FINAL (11) QUE SO VAI IR ATÉ O 10 E QUANTO QUE VAI SER SOMADO, NESTE CASO DE 3 EM 3

for rodada in range(1,total_de_tentativas + 1):
    """ Para digitar sem ter que ficar concatenando usamos "{}.format NOMEVARIAVEL", igual a `${nome da variavel}` em JS
    CASO QUEIRA UTILIZAR O SEGUNDO ITEM NO PRIMEIRO {} VOCÊ PODE COLOCAR O INDICE DESTE ELEMENTO, FICANDO 
    "Tentativa {1} de {0}".format(rodada, total_de_tentativas)
    PRINTANDO: Tentativa {total_de_tentativas} de {rodada}
    PARA UMA FORMATAÇÃO DE DINHEIRO PODEMOS USAR 
    R$ {:07.2f}.format(4,5)
    neste caso os dois pontos e F servem para indicar que é um parametro float, o 07 significa que são 7 caracteres o numero todo e caso exista algum espaço vazio ele será preenchido por 0 e o .2 significa que só vão ter 2 casas depois do ponto, assim restringindo e colocando 0 caso não haja
    Esta formatação também serve para números inteiros, colocando D ao invés de F
    Como número inteiro isto serve para utilizar em datas, colcoando de forma mais completa e bonita"""
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        # O CONTINUE FAZ COM QUE VOLTE PARA O INICIO DO FOR, ASSIM NÃO QUEBRANDO O FOR E NEM SEGUINDO O RESTO MESMO ESTANDO ERRADO
        continue

    """ Necessário mudar o valor da variavel pois ela vem como string e não 
    se pode fazer comparação de uma string com uma num pois sempre dará false """

    """ SIGNIFICA QUE SE A VARIAVEL ABAIXO FOR VERDADEIRA ENTÃO IRÁ EXECUTAR O IF"""
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto")

            """ A ELIF É BASICAMENTE A MESMA COISA QUE UM ELSE IF EM JS, ALÉM DE QUE O ELSE 
            NÃO ACEITA CONDIÇÕES, ENTÃO PARA ISSO TEMOS QUE USAR O ELIF"""
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto")

        rodada += 1
        pontos_perdidos = abs((numero_secreto - chute))
        pontos = pontos - pontos_perdidos
print("Fim de jogo!")