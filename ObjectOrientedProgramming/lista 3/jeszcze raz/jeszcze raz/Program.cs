using System;

class Wector
{
    public float[] reprezentacja = { };
    int wymiar;

    public Wector(int rozmiar)
    {
        float[] tablica = new float [rozmiar];
        wymiar = rozmiar;
        reprezentacja = tablica;
    }

    public void dodawanie(Wector b)
    {
        for (int i = 0; i < wymiar; i++)
        {
            this.reprezentacja[i] = b.reprezentacja[i] + this.reprezentacja[i];
        }
    }

    public float iloczynskalarny(Wector b)
    {
        float wynik = 0;
        for (int i = 0; i < this.wymiar; i++)
        {
            wynik = wynik + this.reprezentacja[i] * b.reprezentacja[i];

        }

        return wynik;
    }

    public float norma()
    {
        double wynik;
        float wynik1;
        wynik = this.iloczynskalarny(this);
        wynik = Math.Sqrt((double)wynik);
        wynik1 = (float)wynik;
        return wynik1;



    }

    public void mnozenieskalar(float skalar)
    {
        for (int i = 0; i < wymiar; i++)
        {
            this.reprezentacja[i] = this.reprezentacja[i] * skalar;
        }
    }
    
}

