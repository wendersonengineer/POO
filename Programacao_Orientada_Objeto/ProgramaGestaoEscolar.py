class Escola:
    def __init__(self, nome, idade, nota1, nota2):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = None

    # Realiza inscrição dos alunos
    def inscricao(self):
        self.nome = input("Nome do aluno: ")
        self.idade = int(input(f"Idade do aluno {self.nome}: "))

    def nota(self):
        self.nota1 = float(input("Digite nota P1 do aluno: "))
        self.nota2 = float(input("Digite nota P2 do aluno: "))

    def calculo(self):
        self.media = (self.nota1 + self.nota2) / 2
        print(f"\nA média do aluno {self.nome} é {self.media:.2f}")

        if self.media >= 7:
            print(f"O aluno {self.nome} está aprovado com média {self.media:.2f}")
        elif self.media >= 4:
            print(f"O aluno {self.nome} está em recuperação com média {self.media:.2f}")
        else:
            print(f"O aluno {self.nome} está reprovado com média {self.media:.2f}")

# Criando uma instância da classe Escola
aluno = Escola()

# Chamando os métodos na ordem correta
aluno.inscricao()
aluno.nota()
aluno.calculo()