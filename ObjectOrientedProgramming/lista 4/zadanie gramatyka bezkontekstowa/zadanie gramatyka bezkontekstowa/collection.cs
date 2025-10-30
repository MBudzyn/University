using System;
using System.ComponentModel.DataAnnotations;


class Lista<T> 
{
    Lista<T> next;
    private T val;
    private int length;

    public int Length
    {
        get
        {
            if (next == null)
                return 1;
            else
            {
                return 1 + next.Length;
            }
        }
    }

  
    public void add(T element)
    {
        if (next == null) 
        {
            next = new Lista<T>();
            next.val = element;
        }
        else 
        {
            next.add(element);
        }
    }
   
    public T this[int indeks] {
        get {
            if (indeks == 0) return val;
            return this.next[indeks - 1];
        }
    }
}

class MojProgram
{
    static Lista<int> t = new Lista<int>();

    


    public static void Main()
    {
        t.add(8);
        t.add(5);
        t.add(8);
        t.add(5);
        Console.WriteLine(t[0]);
        Console.WriteLine(t[1]);
        Console.WriteLine(t[2]);
        Console.WriteLine(t[3]);
        Console.WriteLine(t[4]);
        Console.WriteLine(t.Length);
     
    }
}