

class Escola:
  
    def __init__(self, nome, idade):
    
        self.nome = nome
        self.idade = idade
        self.nota1 = None
        self.nota2 = None
        self.nota_final = None 

    def nota(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def calculo(self):

        self.nota_final = (self.nota1 + self.nota2) /2

        if self.nota_final >= 7:
            print(f"O aluno(a {self.nome} foi aprovado com sucesso! Media final: {self.nota_final:.2f}.")

        elif self.nota_final >= 4 and self.nota_final < 7:
            print(f"O aluno(a) {self.nome} ficou em recuperação! Média final: {self.nota_final:.2f}.")

        else:
            print(f"O aluno(a) {self.nome} foi reprovado ! Média final: {self.nota_final:.2f}.")

    def apresentacao(self):
        print(f"Aluno(a) {self.nome}") 
    




