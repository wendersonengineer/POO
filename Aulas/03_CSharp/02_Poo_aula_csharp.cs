using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Introducao_C_Sharp
{
    public class Poo_aula_csharp
    {
        static void Main(string[] args)
        {
            //Criando variaveis com instâncias da classe Pessoa
            Pessoa p1 = new Pessoa("Diego", "Inácio", 35);
            Pessoa p2 = new Pessoa("Maria", "Silva", 20);

            // Exibindo os dados
            Console.WriteLine($"Pessoa 1: {p1.Nome} - {p1.Sobrenome} - {p1.Idade} anos.");
            Console.WriteLine($"Pessoa 2: {p2.Nome} - {p2.Sobrenome} - {p1.Idade} anos.");

        }
    }
}
