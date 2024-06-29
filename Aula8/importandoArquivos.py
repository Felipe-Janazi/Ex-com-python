# Para fazer com que funcione é necessário definir uma função nos arquivos dos jogos, após isso importar o nome do arquivo neste documento e depois colocar o nome do arquivo . a função que está definida no jogo.
import forca
import niveis

def escolha_jogo():
    print("************************************")
    print("********* Escolha seu jogo *********")
    print("************************************")

    print("[1] Forca [2] Adivinhacao")
    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("jogando forca")
        forca.jogar_forca()
    if (jogo == 2): 
        print("Jogando adivinhacao")
        niveis.jogar_adivinhacao()

if (__nome__ == "__main__"):
    escolha_jogo()