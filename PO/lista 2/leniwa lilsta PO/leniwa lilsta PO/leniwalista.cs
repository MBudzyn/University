
 using System;
 using System.Numerics;
 using System.Runtime.CompilerServices;
 using System.Runtime.InteropServices;

 /*
# Mateusz Budzyński
# lista 2 zadanie 4 klasa leniwa lista
*/






 class leniwatablica
 {
     Random generator = new Random();
     public int[] tablica = {};

     public int zwroc(int indeks)
     {
         if (tablica.Length <= indeks)
         {
             if (tablica.Length == 0)
             {
                 int[] zmienna = { 0 };
                 tablica = zmienna;
             }

             int[] nowa = new int[indeks];
             for (int i = 0; i < nowa.Length; i++)
             {
                 if (i < tablica.Length)
                     nowa[i] = tablica[i];
                 else
                     nowa[i] = nowa[i - 1] + 1;
             }

             tablica = nowa;
         }
         return tablica[indeks-1];
     }
     bool czypierwsza(int i)
     {
         if (i == 1)
             return false;
         if (i == 0)
             return false;
         if (i == 2)
             return true;
         for (int j = 2; j * j <= i; j++)
         {
             if (i % j == 0)
                 return false;
         }

         return true;

     }

     public int size()
     {
         return tablica.Length;
     }
 }
 class pierwsza : leniwatablica
 {
    
     public int[] tablica = {};

     public int zwroc(int indeks)
     {
         bool warunek = true;
         if (tablica.Length <= indeks)
         {
             if (tablica.Length == 0)
             {
                 int[] zmienna = { 2 };
                 tablica = zmienna;
             }

             int[] nowa = new int[indeks];
             for (int i = 0; i < nowa.Length; i++)
             {
                 if (i < tablica.Length)
                     nowa[i] = tablica[i];
                 else
                 {
                     int k = nowa[i - 1]+1;
                     warunek = true;
                     while (warunek)
                     {
                         if (czypierwsza(k) == true)
                         {
                             nowa[i] = k;
                             warunek = false;
                         }
                         else
                         {
                             k = k + 1;
                         }



                     }
                     
                     
                 }
                     
             }

             tablica = nowa;
         }
         return tablica[indeks-1];
     }
     bool czypierwsza(int i)
     {
         if (i == 1)
             return false;
         if (i == 0)
             return false;
         if (i == 2)
             return true;
         for (int j = 2; j * j <= i; j++)
         {
             if (i % j == 0)
                 return false;
         }

         return true;

     }
     
 }




 class MojProgram
     {
         
         public static leniwatablica z = new leniwatablica();
         public static pierwsza t = new pierwsza();
         
         
         public static void Main()
         {
             Console.WriteLine(z.zwroc(4));
             Console.WriteLine(z.zwroc(5));
             Console.WriteLine(z.zwroc(6));
             Console.WriteLine(z.zwroc(7));
             Console.WriteLine(z.zwroc(8));
             Console.WriteLine(z.zwroc(9));
             Console.WriteLine(z.zwroc(4));
             Console.WriteLine(z.size());
             
             Console.WriteLine(t.zwroc(6));
             
             Console.WriteLine(z.zwroc(5));
             


         }
     }
 
 