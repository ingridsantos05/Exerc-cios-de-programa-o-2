#Faça um programa que peça um número inteiro e determine se ele é ou não
#um número primo. Um número primo é aquele que é divisível somente por ele
#mesmo e por 1.
def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
        return True
num = int(input("Digite um número inteiro: "))
if primo(num):
    print(f"O numero {num} é primo.")
else:
    print(f"O número {num} não é primo. ")
