#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu nome: ")
if len(nome) <= 3:
    print("Erro: O nome deve ter mais de 3 caracteres.")

idade = int(input("Digite sua idade: "))
if idade < 0 or idade > 150:
    print("Erro: A idade deve estar entre 0 e 150 anos.")

salario = float(input("digite seu salário: "))
if salario <= 0:
    print("Erro: O salario deve ser maior que zero.")

sexo = input("Digite seu sexo (f/m): ").lower()
if sexo not in ['f', 'm']:
    print("Erro: O sexo deve ser 'f' ou 'm'.")

estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
if estado_civil not in ['s', 'c', 'v', 'd']:
    print("Erro: Estado civil inválido. Digite 's', 'c', 'v' ou 'd'.")

print("\nCadastro realizado com sucesso!")
print("Nome:", nome)
print("Idade:", idade)
print("Salário: R$", salario)
print("Sexo:", sexo.upper())
print("Estado Civil:", estado_civil.upper())
