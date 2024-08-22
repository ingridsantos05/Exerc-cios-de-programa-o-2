#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
#As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da
#pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
#deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
#"Assassino". Caso contrário, ele será classificado como "Inocente

print("Responda ás perguntas abaixocom 'sim' ou 'não'. ")

respostas_positivas = 0

pergunta = input("Telefonou para a vítima? ")
pergunta = input("Esteve no local do crime? ")
pergunta = input("Mora perto da vítima? ")
pergunta = input("Devia para a vítima? ")
pergunta = input("Já trabalhou com a vítima? ")

if respostas_positivas == 2:
    print("classificação: suspeita")
elif 3<= respostas_positivas <=4:
    print("classificação: cuúmplice")
elif respostas_positivas == 5:
    print("classificação: Assassino")
else:
    print("classificação: inocente")