import random
def jogar_advinhação():

    rodada = 1
    numero_secreto = (round(random.randrange(1, 10)*10))
    pontos = 100
    print ("*******************************")
    print ("******Jogo da Adivinhação******")
    print ("*******************************")

    print ("escolha a dificudade")
    dificuldade = int(input("facíl = 1, medio = 2 e difícil = 3: "))

    if (dificuldade == 1):
        total_de_tentativas = 15
    
    elif (dificuldade == 2):
        total_de_tentativas = 10
    
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format (rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if (chute < 1 or chute > 10):
            print ("você deve digitar um número entre 1 e 10") 
            continue
        if (acertou):
            print("Você acertou!")
            break
        
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = (abs(pontos - chute))
            pontos = pontos - pontos_perdidos


    print("Fim do jogo")
    print ("sua pontuação foi ", pontos)
if(__name__ == "__main__"):   
    jogar_advinhação() 