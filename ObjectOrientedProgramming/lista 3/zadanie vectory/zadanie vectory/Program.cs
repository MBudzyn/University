
using System;

 class Wector
{
    public int[] reprezentacja = { };

    public Wector(int rozmiar)
    {
        int[] tablica = new int [rozmiar];
        reprezentacja = tablica;
    }

    
}



class MojProgram
{
    static Wector w1 = new Wector(12);
    
    
    public static void Main()
    {
        w1.reprezentacja[3] = 34;
        Console.WriteLine(w1.reprezentacja[3]);
    }
}