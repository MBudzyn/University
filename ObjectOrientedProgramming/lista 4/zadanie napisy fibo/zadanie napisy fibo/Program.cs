using System.Collections;
/*
 * Mateusz Budzynski
 * lista 4 zadanie fibo
 */

class Element
    {
        public string val;
        public Element next;
    }
class Slowofibo : IEnumerator, IEnumerable
    { 
        Element lista;
        private Element current;
        
        public Slowofibo(int liczba)
        {
            string pierwszy = "b";
            string drugi = "a";
            string pom;
            Element t = new Element();
            this.lista = t;
            for (int i = 0; i < liczba; i++)
            {
                if (i == 0)
                {
                    t.val = pierwszy;
                    t.next = new Element();
                }

                else if (i == 1)
                {
                    t.next = new Element();
                    t.next.val = drugi;
                    
                }
                else
                {
                    while (t.next != null)
                        t = t.next;
                    t.next = new Element();
                    t.next.val = drugi + pierwszy;
                    pom = drugi;
                    drugi = drugi + pierwszy;
                    pierwszy = pom;
                    
                }




            }
            
        }

        
        public bool MoveNext()
        {
            if (this.current == null) this.current = this.lista;
            else this.current = this.current.next;
            return this.current != null;
        }

        public object Current
        {
            get { return current.val; }
        }

        public void Reset()
        {
            this.current = this.lista;
        }
        
        public IEnumerator GetEnumerator()
        {
            return this;
        }
        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

    }
    

class MojProgram
{
    static Slowofibo t = new Slowofibo(6);
    static Slowofibo a = new Slowofibo(10);
    static Slowofibo b = new Slowofibo(3);
    
    public static void Main()
    {
        
        foreach (string e in t)
        {
            Console.WriteLine(e);
        }
        Console.WriteLine();
        foreach (string e in a)
        {
            Console.WriteLine(e);
        }
        Console.WriteLine();
        foreach (string e in b)
        {
            Console.WriteLine(e);
        }
    }
}