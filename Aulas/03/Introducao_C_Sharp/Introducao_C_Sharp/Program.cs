public class Pessoa

{   // Definindo os nomes dos atributos
    public string Nome { get; set; }
    public string Sobrenome { get; set; }

    public int Idade { get; set; }

    public Pessoa(string nome, string sobrenome, int idade)

    // Construtor

    {
        Nome = nome;
        Sobrenome = sobrenome;
        Idade = idade;
    }

}
