# Nas estruturas de repetição, temos dois modelos comumente usados, sendo eles o FOR e o WHILE.

# Para o laço for, usamos um parâmetro numérico em que o código irá se repetir. Após atingir a quantidade de repetições requerida, o script se encerra. Agora vamos ao exemplo:

# Imagine que você é um professor e precisa listar as notas de seus alunos para o sistema

notas = [] # Aqui eu crio uma lista vazia que irá armazenas as informações finais inseridas pelo usuário

nomeDoAluno = input("Informe o nome do aluno: ")
nota = float( input("Informe a nota do aluno: ") )
resultado = [nomeDoAluno, nota] # Aqui eu crio uma lista que irá armazenar o nome e a nota do aluno

notas.append(resultado) # Aqui eu estou adicionando (append) uma lista dentro de outra lista. a lista armazenada anteriormente na variável resultado, que contém o nome e a nota de cada aluno, será armazenada dentro da variável notas, que no final, conterá várias listas, cada uma com o nome de um aluno e sua respectiva nota

# Agora imagine que você tenha 40 alunos nesta sala. Você fará este processo 40 vezes? Para facilitar isso, usaremos o laço de repetição FOR:

notas = []

for x in range(4):
    nomeDoAluno = str(input("Nome do aluno: ") )
    nota = float( input("Nota do aluno: ") )
    resultado = [nomeDoAluno, nota]
    notas.append(resultado)

print("quantidade de notas", len(notas)) # A função len, serve para mostrar quantos index eu tenho preenchido dentro dessa lista. No caso, como nosso laço se repete por 4 vezes, teremos 4 notas.

# Agora faremos outro laço de repetição, desta vez percorrendo a lista (notas) que populamos anteriormente, para listar, em fim, os alunos e suas notas.

for n in notas:
    nomeDoAluno = n[0] # Em uma lista, os valores armazenados recebem o nome de index. O primeiro index de uma lsita sempre inicia pelo 0. Então, estamos dizendo pro script que o nome do aluno, está armazenado no index 0 da lista notas.

    nota = n[1] # Aqui, seguimos o mesmo conceito. Anteriormente, armazenamos a nota do respectivo aluno no index 1 da lista notas.

    print("O aluno", nomeDoAluno, "tirou a nota:", nota)


# O laço de repetição WHILE consiste em repetir um bloco de códigos ENQUANTO o parâmetro passado for verdadeiro. Veja como podemos replicar o script acima usando o while
    
notas = []

contador = 0 # Esta variável servirá de condição para nosso laço

while contador < 5:
    nomeDoAluno = str(input("Nome do aluno: "))
    nota = float(input("Nota do aluno: "))
    resultado = [nomeDoAluno, nota]
    notas.append(resultado)

    contador += 1 # Isto é a mesma coisa que contador = contador + 1 (A cada repetição do laço, incrementará 1 ao valor da variável contador. Quando atingir o valor 5, ele sessará a repetição.)
