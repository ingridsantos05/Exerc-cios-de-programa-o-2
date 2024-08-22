#1º Crie um programa em Python que peça dois números ao usuário. Em
#seguida, você vai mostrar a soma, subtração, multiplicação, divisão,
#exponenciação e resto da divisão do primeiro número pelo segundo.

num1= int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))

resultado_soma = num1 + num2
resultado_subtração = num1 - num2
resultado_multiplicação = num1 * num2
resultado_divisão = "indefinido"
resultado = num1 ** num2

resultado_divisão = num1 / num2 
resultado_resto = num1 % num2

print(f"Soma:{resultado_soma}")
print(f"Subtração:{resultado_subtração}")
print(f"Multiplicação:{resultado_multiplicação}")
print(f"Divisão:{resultado_divisão}")
print(f"resultado:{resultado}")

