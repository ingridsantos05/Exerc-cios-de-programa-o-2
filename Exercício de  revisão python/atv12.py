#Faça um programa que, dado um conjunto de N números, determine o menor
#valor, o maior valor e a soma dos valores.
N = int(input("Digite a quantidade de números a serem inseridos: "))
menor = float('inf')
maior = float('-inf')
soma = 0

for i in range(N):
    numero = float(input(f"Digite o {i+1}º numero: "))
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero
    soma += numero
print(f"\nMenor valor: {menor}")
print(f"\nMaior valor: {maior}")
print(f"\nSoma dos valores: {soma}")