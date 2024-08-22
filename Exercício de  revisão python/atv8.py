#Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou PCD.
#Escreva um programa que pergunta a situação do usuário (se é idoso, se é
#gestante, se é PCD ou nenhum destes) e diga se ele pode ter acesso a fila
#prioridade ou não.
print("situações possiveis:")
print("1 - Idoso")
print("2 - Gestante")
print("3 - Pessoa com deficiência")
print("4 - Nenhum destes")

Situação = int(input("Digite á sua situação: "))

if Situação == 1 or Situação == 2 or Situação == 3:
    print("Você pode ter acesso á fila prioritária.")
elif Situação == 4:
    print("Você não tem acesso á fila prioritária.")
else:
    print("Opção inválida. por favor, escolha uma das opções válidas (1 a 4).")