class chave:
    def __init__(self, status):
        self.gira = False
        self.status = status

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.item = None #nulo

    #Metodo de pegar a chave e incluir no item
    def pegar(self, chave:chave):
        if self.item == None:
            self.item = chave

    def movimenta(self):
        if not self.item.gira:
            self.item.gira = True
            print(f"O {self.nome} girou a chave!")
        else:
            print("A chave já foi girada")

p1 = Pessoa("Diego", 30)

ch = chave("Definida")


p1.pegar(ch)

print(p1.item.status)

p1.movimenta()
p1.movimenta()

