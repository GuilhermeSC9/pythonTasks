# O modelo de tomada de decisão em python é muito simples, tendo como base as tags de if, elif e else

# Neste primeiro exemplo, faremos uma verificação simples, simulando uma entrada de balada para maiores de idade

idade = int( input("Informe sua idade: ") )

if idade >= 18:
    print("Entrada permitida!")

else:
    print("Entrada negada!")

# Para criarmos uma verificação com mais de duas condições, podemos usar o elif. Veja:
    
    salario = float( input("Informe seu salário: ") )

    if salario > 0 and salario <= 3000:
        print("Você é programador júnior.")

    elif salario > 3000 and salario <= 6000:
        print("Você é programador pleno.")

    else:
        print("Você é programador sênior.")

# Repare que eu não passo nenhuma condição no último else, porque o script só irá executar essa linha, caso as duas anteriores sejam falas. Porém nada impede que você crie outras condicionais antes deste último else, basta repetir a estrutura de elif.