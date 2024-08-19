# Papel Pedra Tesoura.

import random
import os

cls = os.system('cls')

escolhas = ["Pedra", "Papel", "Tesoura"]
jogada_pc =  random.choice(escolhas)
jogada_humana = input("Escolha uma jogada: [1] = Pedra | [2] = Papel | [3] = Tesoura: ")
print()


match jogada_humana:
    case '1':
        jogada_humana = "Pedra"
    case '2':
        jogada_humana = 'Papel'
    case '3':
        jogada_humana = 'Tesoura'
    case _:
        print("Esta não é uma jogada válida...")

 
print(f"Jogada PC: {jogada_pc}")
print(f"Jogada Humana: {jogada_humana} \n")


if jogada_humana == jogada_pc:
    print("Empatou!")
elif jogada_humana == 'Pedra' and jogada_pc == 'Tesoura':
    print("Você Ganhou!")
elif jogada_humana == 'Papel' and jogada_pc == 'Pedra':
    print("Você Ganhou!")
elif jogada_humana == 'Tesoura' and jogada_pc == 'Papel':
    print("Você Ganhou!")
else:
    print("Computador Ganhou!")

