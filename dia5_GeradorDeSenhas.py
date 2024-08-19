# Gerador de Senhas

import os
import random
cls = os.system('cls')

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "z",
          "A", "B", "C", "D", "E", "F", "G", "H", "I", "j", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"]
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
simbolos = ["!", "@", "#", "%", "&"]

senha = ""
senha_forte = ""

qtd_letras = int(input("Informe  quantidade de letras que você deseja na senha: "))
qtd_numeros = int(input("Informe  quantidade de números que você deseja na senha: "))
qtd_simbolos = int(input("Informe  quantidade de símbolos que você deseja na senha: "))


for letra in range(1, qtd_letras + 1):
    rand_letra = random.choice(letras)
    senha += rand_letra

for numero in range(1, qtd_numeros + 1):
    rand_numeros = random.choice(numeros)
    senha += str(rand_numeros)
    
for simbolo in range(1, qtd_simbolos +1):
    rand_simbolo = random.choice(simbolos)
    senha += rand_simbolo

# Randomizando a senha e embaralhando as letras e mnumeros
for letra in range(1,len(senha) +1):
    rand_senha = random.choice(senha)
    senha_forte += rand_senha
    

print(senha_forte)
