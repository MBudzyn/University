/*
 * Mateusz Budzyński
 * lista 3 zadanie wektory
 * net 7.0
 * napisane w srodowisku rider konfiguracja solution
 */

namespace jeszcze_raz;
using System;

class MojProgram
{
    static Wector w1 = new Wector(3);
    static Wector w2 = new Wector(6);
    static Wector w3 = new Wector(11);
    
    public static void Main()
    {
        for(int i=0; i<3;i++)
        {
            w1.reprezentacja[i] = i;
        }
        for(int i=11; i<17;i++)
        {
            w2.reprezentacja[i-11] = i;
        }
        for(int i=-20; i<-9;i++)
        {
            w3.reprezentacja[i+20] = i;
        }
        Console.Write("wector w1: ");
        for(int i=0; i<3;i++)
        {
            Console.Write(w1.reprezentacja[i] + " ");
        }
        Console.WriteLine();
        Console.Write("wector w2: ");
        for(int i=0; i<6;i++)
        {
            Console.Write(w2.reprezentacja[i] + " ");
        }
        Console.WriteLine();
        Console.Write("wector w3: ");
        for(int i=0; i<11;i++)
        {
            Console.Write(w3.reprezentacja[i] + " ");
        }
        Console.WriteLine();
        Console.WriteLine();
        Console.WriteLine("iloczyn skalarny wectorow w1 i w2: "+ w1.iloczynskalarny(w2));
        Console.WriteLine("iloczyn skalarny wectorow w1 i w3: "+ w1.iloczynskalarny(w3));
        Console.WriteLine("iloczyn skalarny wectorow w2 i w3: "+ w2.iloczynskalarny(w3));
        Console.WriteLine();
        Console.WriteLine("dlugosc wectora w1: "+ w1.norma());
        Console.WriteLine("dlugosc wectora w2: "+ w2.norma());
        Console.WriteLine("dlugosc wectora w3: "+ w3.norma());
        Console.WriteLine();
        

        
    }
}