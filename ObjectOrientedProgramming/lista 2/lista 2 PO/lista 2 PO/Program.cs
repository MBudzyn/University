
 using System;
 using System.Runtime.CompilerServices;
 using System.Runtime.InteropServices;
 
 
 
 /*
# Mateusz Budzyński
# lista 2 zadanie 1 klasa intstream
*/



 class intstream
 {
     public int wartosc = -1;
     public bool es = false;

     public bool eos()
     {
         return es;
     }
     public int next()
     {
         try
         {
             wartosc = wartosc + 1;
             return wartosc;
         }
         catch
         {
             es = true;
             return wartosc-1;
         }
         
         
     }

     public void reset()
     {
         wartosc = -1;
     }

 }

 class losoweintstream : pierwszeintstream
 {
     Random generator = new Random();
     public int next()
     {
         wartosc = generator.Next();
         return wartosc;
     }
     
 }

 class pierwszeintstream : intstream
 {
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

     private bool t = true;

     public int next()
     {
         try
         {
             while (t)
             {
                 int i = wartosc + 1;
                 if (czypierwsza(i) == true)
                 {
                     wartosc = i;
                     return wartosc;
                 }
                 else
                 {
                     wartosc = wartosc + 1;
                 }
             }

         }
         catch
         {
             es = true;
         }

         return wartosc;
     }
 }

 class RandomWordStream : losoweintstream
 {
     
     
     
     
 }
 
 class MojProgram
     {
         Random generator = new Random();
         public static intstream z = new intstream();
         public static pierwszeintstream k = new pierwszeintstream();
         public static losoweintstream w = new losoweintstream();

         public static void Main()
         {
             Console.WriteLine(k.next());
             Console.WriteLine(k.next());
             Console.WriteLine(k.next());
             Console.WriteLine(k.next());
             Console.WriteLine(w.next());
             Console.WriteLine(w.next());
             Console.WriteLine(w.next());
             Console.WriteLine(w.next());
             k.reset();
             Console.WriteLine(k.next());
             Console.WriteLine(k.next());
             Console.WriteLine(k.next());
             Console.WriteLine(k.next());
             
             Console.WriteLine(z.next());
             Console.WriteLine(z.next());
             Console.WriteLine(z.next());
             Console.WriteLine(z.next());
             z.reset();
             Console.WriteLine(z.next());
             Console.WriteLine(z.next());
             
         }
     }
 
 