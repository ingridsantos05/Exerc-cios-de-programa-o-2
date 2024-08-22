# Crie um sistema para um aplicativo bancário, que possui a classe conta bancaria com as seguintes caracteristicas:
# Atributo: titulo, saldo, numero_conta e tipo_conta. 
# Métodos: depositar, sacar, transferir e verificar_saldo. 
# OBS: após cada alteração no saldo , exiba o novo valor na tela.
class conta_bancaria:
    def __init__ (self, numero_conta, tipo_conta, titular, saldo_inicial):
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        self.titulo = titular
        self.saldo = saldo_inicial

    def depositar(self):
        deposito = float(input("Digite o valor para depósito: "))
        self.saldo += deposito
        print(f"O valor do depósito é: {self.saldo:.2f}")
    
    def sacar(self):
        sac = float(input("Digite o valor para saque: "))
        self.saldo += sac
        print(f"O valor do seu saldo é: {self.saldo:.2f}")
    
    def transferir(self, saldo_de_ingrid):
        valor = float(input("digite o valor para trasferir: "))
        self.saldo -= valor
        saldo_de_ingrid += valor
        return saldo_de_ingrid
   
    
    def transferir1(self, saldo_de_edvan):
        valor = float(input("digite o valor para saque: "))
        self.saldo -= valor
        saldo_de_edvan += valor
        return saldo_de_edvan
    
    def verificar_saldo(self):
        print(f"saldo atual da conta de edvan: R${conta2.saldo:.2f}")

        print(f"saldo atual da conta de ingrid: R${conta1.saldo:.2f}")

conta1 = conta_bancaria("123456", "poupança", "ingrid santos", 150) #250 - 100 = 50
conta2 = conta_bancaria("123456", "corrente", "edvan oliveira", 200) #100 = 300



conta1.depositar()
print(conta1.saldo)

conta2.sacar()
print(conta2.saldo)

print(f"O saldo de edvan após saque: R${conta2.saldo}")

#print(f"O saldo de ingrid atual: R${conta1.saldo:.2f}")




