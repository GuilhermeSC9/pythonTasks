from random import randint

N = 0
Placar1 = 0
Placar2 = 0

while N <= 5:
    firstRandomPoint = randint(1, 10)
    secondRandomPoint = randint(1, 10)

    print(f"O primeiro número é: {firstRandomPoint}")
    print(f"O segundo número é: {secondRandomPoint}")

    if firstRandomPoint == secondRandomPoint:
        print("Empate")
    elif firstRandomPoint > secondRandomPoint:
        print("Ponto para a IA 1!")
        Placar1 += 1
    elif firstRandomPoint < secondRandomPoint:
        print("Ponto para a IA 2!")
        Placar2 += 1

    print(f"Pontos da IA 1: {Placar1}")
    print(f"Pontos da IA 2: {Placar2}\n")
    N += 1

print("\nPontuação final:")
print(f"Pontos do IA 1: {Placar1}")
print(f"Pontos da IA 2: {Placar2}")