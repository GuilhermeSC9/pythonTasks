from random import randint
Y = 0
N = 0
repeatedList = []
numberChoosed = []
score1 = 0
score2 = 0
def rangeVerify(userNumber):
    while userNumber not in range (1, 11):
        userNumber = int(input("O número tem que ser entre 1 e 10. Digite novamente: "))

while N <= 5:
    randomNumber = randint(1, 10)
    userNumber = int(input("Digite um número de 1 a 10: "))

    rangeVerify(userNumber)
    
        
    numberRepeated = userNumber
    while N >= 1 and numberRepeated == userNumber or userNumber not in range(1, 11):
        userNumber = int(input("Este número já foi selecionado ou não está entre 1 e 10. Escolha outro: ")) 
        numberChoosed.append(userNumber)

            
    print(f"\nNúmero escolhido por IA: {randomNumber}")
    print(f"Número escolhiodo pelo usuário: {userNumber}")

    if randomNumber == userNumber:
        print("Empate!")
    elif randomNumber > userNumber:
        print("Ponto para a IA!")
        score1 +=1
    elif randomNumber < userNumber:
        print("Ponto para o usuário!")
        score2 +=1

    print(f"\nTotal de pontos da IA: {score1}")
    print(f"Total de pontos do usuário: {score2}")
    print(f"\nOs números já digitados pelo usuário são: {numberChoosed}")
    N += 1
if N == 6 and score1 == score2:
    print("O jogo deu empate! Vamos recomeçar: \n\n")
    N = 0

print("\nPontuação final:")
print(f"Pontuação da IA: {score1}")
print(f"Pontuação do usuário: {score2}")