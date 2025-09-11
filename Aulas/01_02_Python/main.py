

from ClasseProduto import Produto as prod
from ProgramaGestaoEscolar1 import Escola as scho

produto1 = prod("Leite", 20.00, 40)
produto2 = prod("Maçã", 9.99, 30)
produto3 = prod("Água", 3.99, 50)

aluno1 = scho("Victor Santos", 36)
aluno2 = scho("Ana Maria", 31)
aluno3 = scho("Joana Dark", 52)

listap = [produto1, produto2, produto3]
listas = [aluno1, aluno2, aluno3]

for i in range(3):
    listas[i].apresentacao(), 
    print("comprou"), listap[i].apresentacao()