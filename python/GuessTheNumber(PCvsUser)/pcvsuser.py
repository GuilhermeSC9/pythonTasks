from random import randint

N = 0
score1 = 0
score2 = 0
userNumberList = []
    # Exemplo de função abaixo:
"""def rangeVerify(userSelect):
    while userSelect not in range(1, 11) or userSelect == None:
        userSelect = int(input("Esse número não é válido. Escolha outro: "))"""

while N <= 5:
    machineNumber = randint(1, 10)
    userSelect = int(input("Insira um número entre 1 e 10: "))
    while userSelect not in range(1, 11) or userSelect == None:
        userSelect = int(input("Esse número não é válido. Escolha outro: "))
    rightNumber = userSelect

    if N == 0:
        userNumberList.append(rightNumber)
    else:
        while userSelect in userNumberList:
            userSelect = int(input("Esse número já foi selecionado. Tente outro: "))
            if userSelect is None:
                continue
            else:
                rightNumber = userSelect
        userNumberList.append(rightNumber)
    
    if machineNumber == rightNumber:
        print("\nEmpate!")
    elif machineNumber > rightNumber:
        print("\nPonto para a máquina!")
        score1 += 1
    elif machineNumber < rightNumber:
        print("\nPonto para o usuário!")
        score2 += 1

    print(f"\nO número selecionado pela máquina é: {machineNumber}")
    print(f"O número selecionado pelo usuário é: {rightNumber}")
    N += 1
if score1 == score2:
    print("\n\n\nO placar final foi EMPATE! Vamos recomeçar: \n\n\n")
    N = 0
    userNumberList.clear()
elif score1 > score2:
    print("\nVitória da máquina!")
else:
    print("\nVitória do usuário!")
print(f"\nO placar final foi de: {score1} a {score2}!")



        