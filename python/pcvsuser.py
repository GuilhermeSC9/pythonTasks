from random import randint

N = 0
Placar1 = 0
Placar2 = 0

while N <= 5:
    randomNumber = randint(1,10)
    userNumber = int(input("Digite um número de 1 a 10: "))
    while userNumber not in range (1, 11):
        int(input("O número tem que ser entre 1 e 10. Digite novamente: "))
        break
    
    print(f"\nNúmero escolhido por IA: {randomNumber}")
    print(f"Número escolhiodo pelo usuário: {userNumber}")

    if randomNumber == userNumber:
        print("Empate!")
    elif randomNumber > userNumber:
        print("Ponto para IA!")
        Placar1 +=1
    elif randomNumber < userNumber:
        print("Ponto para o usuário!")
        Placar2 +=1

    print(f"\nTotal de pontos da IA: {Placar1}")
    print(f"Total de pontos do usuário: {Placar2}")
    N += 1

print("\nPontuação final:")
print(f"Pontuação da IA: {Placar1}")
print(f"Pontuação do usuário: {Placar2}")