
class Produto:
    def __init__(self, nome, preco, quantidade):
        
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    # Método de Apresentação
    def apresentacao(self):
        print(f"Nome do Produto: {self.nome}\nPreço R$ {self.preco}\nQuantidade: {self.quantidade}")

# Criando objetos
produto1 = Produto("Leite", 7.99, 10)
produto2 = Produto("Maçã", 0.99, 15)
produto3 = Produto("Água", 1.99, 20)


    
        




    