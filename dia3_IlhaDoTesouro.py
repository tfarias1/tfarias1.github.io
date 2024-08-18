# Projeto - Ilha do Tesouro

print('''
      
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************  
  
''')

print("Bem vindo a Ilha do Tesouro. Sua missão é encontrar o baú do tesouro!")
lado = input("Você está na pista do Tesouro, você escolhe percorrer qual lado da ilha?"
             "(Pressione 'D') para Direito ou (Pressione 'E') para Esquerdo ").upper()

if lado == "D":
    rio = input("Agora você precisa atravessar um rio com piratas. "
                "Você espera eles irem embora ( Pressione 'E') ou (Pressiona 'A' para atravessa mesmo assim?  ").upper()
    
    if rio == "E":
        porta = int(input("Você encontrou 4 portas, faça sua escolha agora para abrir: "
                          "Vermelha (Pressione '1') | Azul (Pressione '2') | Amarela (Pressione '3') "))
        if porta == 1:
            print ("Você foi queimado. GAME OVER!")
        elif porta == 2:
            print("Você foi comido por uma fera. GAME OVER!")
        elif porta == 3:
            print("Você encontrou o tesouro... PARABÉNS!")
        else:
            print("Os piratas te acharam. GAME OVER!")

elif lado == "D":
    print("Você caiu em um buraco, GAME OVER!")
else:
    print("Você foi morto por um tigre, GAME OVER!")