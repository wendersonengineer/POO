📘 Aula de C# – Introdução à Programação Orientada a Objetos (POO)
Este projeto demonstra os conceitos básicos de Programação Orientada a Objetos (POO) em C#, utilizando a criação de uma classe chamada Pessoa e instanciando objetos dessa classe.

🧠 Objetivos da Aula
Compreender o que é uma classe e como ela representa um modelo de objeto.

Aprender a declarar atributos e métodos.

Utilizar construtores para inicializar objetos.

Criar instâncias de uma classe.

Exibir dados de objetos no console.

🏗️ Estrutura do Código
Classe Pessoa

public class Pessoa
```CSharp
{
    public string Nome { get; set; }
    public string Sobrenome { get; set; }
    public int Idade { get; set; }

    public Pessoa(string nome, string sobrenome, int idade)
    {
        Nome = nome;
        Sobrenome = sobrenome;
        Idade = idade;
    }
}

. Atributos: Nome, Sobrenome e Idade.

. Construtor: Recebe os valores iniciais e os atribui aos atributos da classe.

---

Classe Principal Poo_aula_csharp
```c
static void Main(string[] args)
{
    Pessoa p1 = new Pessoa("Diego", "Inácio", 35);
    Pessoa p2 = new Pessoa("Maria", "Silva", 20);

    Console.WriteLine($"Pessoa 1: {p1.Nome} - {p1.Sobrenome} - {p1.Idade} anos.");
    Console.WriteLine($"Pessoa 2: {p2.Nome} - {p2.Sobrenome} - {p1.Idade} anos.");
}

. Instanciação: Criação de dois objetos Pessoa.

. Exibição: Impressão dos dados no console.

Console.WriteLine($"Pessoa 2: {p2.Nome} - {p2.Sobrenome} - {p2.Idade} anos.");


✅ Conceitos Aprendidos
. Como definir uma classe com atributos e construtor.

. Como instanciar objetos e acessar seus dados.

. Como utilizar interpolação de strings para exibir informações.

🚀 Próximos Passos
. Adicionar métodos à classe Pessoa, como Apresentar().

. Trabalhar com listas de objetos.

. Explorar herança e polimorfismo.