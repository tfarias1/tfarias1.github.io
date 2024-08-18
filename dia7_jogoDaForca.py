import os
import random

cls = os.system('cls')
print("Bem vindo ao jogo da forca, descubra a palavra misteriosa! \n")

# Desenhando a Forca
forca = ['''
 _______  
|       |
| 
| 
|
| 
''',

'''
 _______  
|       |
|      ( ) 
|       
|     
|
''',

'''
 _______  
|       |
|      ( ) 
|       | 
|     
| 
''',

'''
 _______  
|       |
|      ( ) 
|    ./ | 
|     
| 
''',

'''
 _______  
|       |
|      ( ) 
|    ./ | \.
|     
| 
''',

'''
 _______  
|       |
|      ( ) 
|    ./ | \.
|     ./ 
| 
''',

'''
 _______  
|       |
|      ( ) 
|    ./ | \.
|     ./ \.
| 
'''
]

# Configura o número inicial de vidas com base no número de estágios da forca
vidas = len(forca) - 1
letras_escolhidas = []
banco_de_palavras = ["Tomate", "Caipira", "Celular", "TikTok", "Supermercado"]
linhas = []

# Selecionando aleatoriamente uma palavra
indice_sorteado = random.randint(0, len(banco_de_palavras) - 1)
palavra_sorteada = banco_de_palavras[indice_sorteado].upper()

# Criando as linhas inferiores
linhas = ["_" for _ in palavra_sorteada]

while vidas > 0:
    cls = os.system('cls')
    print(f'Letras Escolhidas: {letras_escolhidas} \n')
    print(forca[len(forca) - 1 - vidas])
    print(f'{" ".join(linhas)} \n \n')
    
    if "_" not in linhas:
        print("Parabéns, você descobriu a palavra!")
        break

    letra = input("Escolha uma letra: ").upper()

    # Verifica se a letra existe na palavra sorteada
    if letra in palavra_sorteada:        
        print(f'Sim, existe a letra "{letra}" na palavra')
        if letra not in letras_escolhidas:
            letras_escolhidas.append(letra)  
            # Substitui as linhas correspondentes à letra correta
            for i, char in enumerate(palavra_sorteada):
                if char == letra:
                    linhas[i] = letra
        else:
            print("Letra já foi escolhida antes!")
         
    else:
        # Se a letra não existir, gastamos uma vida!
        print(f'Não existe a letra {letra} na palavra')
        if letra not in letras_escolhidas:
            letras_escolhidas.append(letra)  
            vidas -= 1  # Decrementa uma vida
        else:
            print("Letra já foi escolhida antes!")           

if vidas == 0:
    print("Game Over! Você perdeu!")
    print(f"A palavra era: {palavra_sorteada}")
