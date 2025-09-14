import time

class Chave:
    def __init__(self, marca):
        self.marca = marca 
        self.ativa = False

    def GirarChave(self):
        if not self.ativa:
            self.ativa = True
            print("A chave foi ativada!")
        else:
            print("A chave já foi ativada!")


class Carro:
    def __init__(self, modelo, ano, cor, potencia, placa, chave: Chave):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.potencia = potencia
        self.placa = placa
        self.ligado = False 
        self.aberto = False 
        self.chave = chave
        self.velocidade = 0

    def AbrirCarro(self, chave):
        if not self.ligado and not self.aberto and self.chave == chave:
            self.aberto = True    
            print(f"O carro esta aberto!")
            self.chave.GirarChave()
        else:
            print(f"O carro já esta aberto ou ligado ou a chave esta errada!")

    def LigarCarro(self):
        if self.aberto and not self.ligado and self.chave.ativa:
            self.ligado = True
            print("O carro esta ligado!")
        elif not self.aberto:
            print("Abra o carro antes de ligar")
        elif not self.chave.ativa:
            print("A chave não foi girada, precisa ativar a chave!")
        else:
            print("O carro esta ligado, rummmmm!")

    def AcelerarCarro(self):
        if self.ligado:
            self.velocidade += 5
            print(f"O carro {self.modelo} está acelerando - Velocidade {self.velocidade} km/h.")
        else:
            print(f"O carro {self.modelo} está desligado - não é possível acelerar no momento!")


    def FrearCarro(self):
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 5
            if self.velocidade < 0:
                self.velocidade = 0
            print(f"O carro {self.modelo} está freando - Velocidade: {self.velocidade} Km/h")
        else:
            print(f"O carro {self.modelo} está parado ou desligado!")

    def FrearTotalmente(self):
        if self.ligado and self.velocidade > 0:
            print(f"O Freio foi acionado totalmente no carro {self.modelo}!")
            while self.velocidade > 0:
                self.FrearCarro()    
                time.sleep(0.5)
            print(f"O carro {self.modelo} parou totamente.")
        else:
            print(f"O carro {self.modelo} já está parado ou desligado!")


    def DesligarCarro(self):
        if not self.ligado:
            print("O carro já está desligado!")
        elif self.velocidade > 0:
            print("Não foi possivel desligar o carro em movimento!")
        else:
            self.ligado = False
            print("O carro foi desligado!")
        
    
            
 
