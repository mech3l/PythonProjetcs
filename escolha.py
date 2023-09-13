import forca
import adivinhação

def jogar_jogos(): 
    print ("*******************************")
    print ("*****Escolha o tipo de jogo****")
    print ("*******************************")

    jogo = int(input("(1) forca, (2) adivinhção: "))

    if (jogo == 1):
        print("jogando forca")
        forca.jogar_forca()

    elif (jogo == 2):
        print("jogando adivinhação")
        adivinhação.jogar_advinhação()

if(__name__ == "__main__"):
    jogar_jogos()