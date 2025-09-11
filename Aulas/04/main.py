from Car import Chave
from Car import Carro

ch = Chave("FIAT")
ch1 = Chave("FERRARI")

car1 = Carro("Uno", 1999, "Verde", 1.0, "KPJ-0077", ch)

# Vai da erro
car1.LigarCarro()

# Vai da certo
car1.AbrirCarro(ch)

# Vai da certo
car1.LigarCarro()

# Acelerar o carro
for i in range(5):
    car1.AcelerarCarro()

# Print --->
print(car1.chave.marca)

# O carro tem que desligar, mas náo pode desligar acelerado
# Tem que ter um méetodo de freiar de 5 em 5
# e tem que ter a inserção da ativação da chave assim que abrir o for True.