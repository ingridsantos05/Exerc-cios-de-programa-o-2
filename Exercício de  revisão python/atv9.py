#Faça um programa que leia um nome de usuário e a sua senha e não aceite
#a senha igual ao nome do usuário, mostrando uma mensagem de erro e
#voltando a pedir as informações.

nome = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if senha == nome:
     print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente. /n")
else:
     print("Cadastro realizado com sucesso!")


