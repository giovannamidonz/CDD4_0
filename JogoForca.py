import random 

palavra = ["kotlin","java","dart","rubi","github"]
palavra = random.choice(palavra)
letra = []
tentativa = 0
chanche = 10
estadoAtual = ["_"]*len(palavra)
letraEscolhida = []


print("Seja bem-vindo, Vamos jogar !?")
print("esse é o jogo da forca\nVocê tem 10 tentativa\n terás uma chance por vez")

while tentativa<= chanche and ''.join(estadoAtual) != palavra:
    letra = str(input("\n\nQual letra você quer tentar ?"))
    while letra in letraEscolhida :
        print(f"você já escolheu {letraEscolhida}")
        letra = str(input("\nQual letra você quer tentar ?"))
        
    letraEscolhida.append(letra)
        
    if letra in palavra:
        print("Parabéns, você acertou!")
        print(f"As letras que você já tentou são : {letraEscolhida}")
        for item in range(len(palavra)):
            if letra == palavra[item]:
                estadoAtual[item]=letra
        print(f"{estadoAtual}")
    else:
        print("que pena você errou!")
        tentativa +=1
        print(f"você já fez, {tentativa} tentativa" )
        print(f"Restam, {chanche-tentativa} chances")
        print(f"{estadoAtual}")
        print(f"As letras que você já tentou são : {letraEscolhida}")
            
if tentativa == chanche:
    print("Voce perdeu")
else :
    print("voce ganhou")