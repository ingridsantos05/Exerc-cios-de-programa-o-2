#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
#se a mesma é uma data válida.

from datetime import datetime

def verifica_data(data):
        try:
            datetime.strptime(Data, "%d/%m/%Y")
            return True 
        except:
            return False
Data = input("Digite uma data no formado dd/mm/aaaa: " )
if verifica_data('data'):
    print("A data é valida.")
else:
    print("A data não é valida.")