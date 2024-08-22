# Desenvolva um sistema de estoque que possui a classe produtos com as seguintes caracteristicas
# Atributos: nome, preço, quantidade e codigo.
# Métodos: calcular_total, atualizar_preço, verificar_disponibilidade.

class Produto:
    def __init__(self, nome, preço, quantidade, codigo):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade
        self.codigo = codigo
    def calcular_total(self):
        return self.preço * self.quantidade
    
    def atualizar_preço(self, novo_preço):
        self.preço = novo_preço

    def verificar_disponibilidade(self):
        return self.quantidade > 0
    
produto1 = Produto("caneta", 1.50, 10, "1234")
print(f"Total para {produto1.nome}: R${produto1.preço:.2f}")

produto1.atualizar_preço(2.00)

print(f"Novo preço do {produto1.nome}: R$ {produto1.preço:.2f}")

if produto1.verificar_disponibilidade():
    print(f"Disponibilidade do {produto1.nome}: {produto1.quantidade}")
else:
    print("\nIndisponivel")



produto2= Produto("caderno", 15.50, 20, "5678")
print(f"Total para {produto2.nome}: R${produto2.preço:.2f}")

produto2.atualizar_preço(17.50)


print(f"Novo preço do {produto2.nome}: R$ {produto2.preço:.2f}")

if produto2.verificar_disponibilidade():
    
    print(f"Disponibilidade do {produto2.nome}: {produto2.quantidade}")
else:
    print("\nIndisponivel")


