from Car import Chave
from Car import Carro


ch = Chave("FIAT")

car1 = Carro("Uno", 1999, "Verde", 1.0, "SQ007", ch)

car1.AbrirCarro(ch)
car1.LigarCarro()

for i in range(6):
    car1.AcelerarCarro()

car1.DesligarCarro()

car1.FrearTotalmente()
car1.DesligarCarro()

#Atividade POO:
# O carro tem que desligar, mas náo pode desligar acelerado
# Tem que ter um método de freiar de 5 em 5
# e tem que ter a inserção da ativação da chave assim que abrir o for True.

