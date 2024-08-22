# 1. Escreva um código que receba o nome de uma pessoa e imprima uma
# saudação personalizada na tela com o nome do usuário.
def saudação(nome):
    nome = nome.capitalize()
    print(f"Seja muito bem vinda(o)! {nome}, que te ver por aqui!")

saudação(input("Digite seu nome: "))