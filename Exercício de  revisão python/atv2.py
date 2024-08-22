#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
 
letra =input("Digite um letra: ").lower()
if letra in 'aeiou':
    print(f"A letra{letra} é uma vogal.")
elif letra.upper():
    print(f"A letra {letra} é uma consoante.")
else:
    print("Você não digitou uma letra válida.")