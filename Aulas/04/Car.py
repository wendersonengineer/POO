class Chave:
    def __init__(self, marca):
        # Método construtor
        self.marca = marca 
        self.ativa = False

# Define a Classe
class Carro:
    def __init__(self, modelo, ano, cor, potencia, placa, chave: Chave):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.potencia = potencia
        self.placa = placa
        self.ligado = False # não precisa ser definido por ser False
        self.aberto = False # não precisa ser definido por ser False
        self.chave = chave
        self.velocidade = 0

    # Métodos  | Ação realizada pela classe
    def AbrirCarro(self, chave):
        if not self.ligado and not self.aberto and self.chave == chave.marca:
            self.aberto = True    # Self.aberto recebe True
            print(f"O carro esta aberto!")
        else:
            print(f"O carro já esta aberto ou ligado ou a chave esta errada!")

    # Método ligar o carro
    def LigarCarro(self):
        if not self.ligado and self.aberto:
            self.ligado = True
            print("O carro esta ligado RUMMMMM!")
        else:
            print("O carro esta ligado ou aberto, verifique isso!")

    # Método Acelerar o carro
    def AcelerarCarro(self):
        if self.ligado and self.velocidade >= 0:
            self.velocidade += 5
            print(f"O carro {self.modelo} velocidade {self.velocidade} km.")
        else:
            print(f"O carro {self.modelo} esta desligado, precisa ligar primeiro!!!")
            
 

#ch = Chave("FIAT")
#car1 = Car("Uno", 1999, "Verde", 1.0, "KPJ-0077", ch)
#car1.AbrirCarro(ch)
#print(car1.chave.marca)