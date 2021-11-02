#Game feito Por Pedro Henrique (PhsTutors)
#Game sendo feito em varias linguagens de programação
#para testar o meu conhecimento!


from random import randint
import time

maquina = randint(0, 10)

opcao = str(input("Escolha Impar ou par: ")).lower()

if opcao == "par" or opcao == "p":
    jogador = int(input("Escolha um numero par: "))
    par = jogador%2
    if par == 0:
        resultado = (jogador + maquina)%2
        if resultado == 0:
            print("Pedra")
            time.sleep(1)
            print("Papel")
            time.sleep(1)
            print("Tesoura")
            print("Voce Ganhou, pois realmente deu par!\n a maquina escolheu", maquina, "e voce escolheu", jogador)
        else:
            print("Pedra")
            time.sleep(1)
            print("Papel")
            time.sleep(1)
            print("Tesoura")
            print("Voce perdeu!\n a maquina escolheu", maquina, "e voce escolheu", jogador)
    else:
        print("Voce escolheu par e colocou numero impar!")
elif opcao == "impar" or opcao == "i":
    jogador = int(input("Escolha um numero Impar: "))
    impar = jogador%2
    if impar != 0:
        resultado = (jogador + maquina)%2
        if resultado > 0:
            print("Pedra")
            time.sleep(1)
            print("Papel")
            time.sleep(1)
            print("Tesoura")
            print("Voce Ganhou, pois realmente deu impar!\n a maquina escolheu", maquina, "e voce escolheu", jogador)
        else:
            print("Pedra")
            time.sleep(1)
            print("Papel")
            time.sleep(1)
            print("Tesoura")
            print("Voce perdeu!o resultado foi Par\n a maquina escolheu", maquina, "e voce escolheu", jogador)
    else:
        print("Voce escolheu impar e colocou numero par!")
else:
    print("Voce nao escolheu impar ou par!")