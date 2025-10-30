using System;

/*
 * Mateusz Budzyński
 * lista 3 zadanie instancje
 * net 7.0
 * napisane w srodowisku rider konfiguracja solution
 */
public class TimeNTon
{
    TimeNTon()
    {
    }

    
    private const int maxlicznik = 6;
    private static TimeNTon instance;
    private static int licznik= 0;
    private static TimeSpan poczatek= new TimeSpan(14, 0, 0);
    private static TimeSpan koniec = new TimeSpan(16, 0, 0);

    
    public static TimeNTon GetInstance()
    {
        if (DateTime.Now.TimeOfDay >= poczatek && DateTime.Now.TimeOfDay <= koniec)
        {
            if (licznik < maxlicznik)
            {
                if (instance == null)
                {
                    instance = new TimeNTon();
                    licznik++;
                }
                return instance;
            }
            else
            {
                return instance;
            }
        }
        else
        {
            if (instance == null)
            {
                instance = new TimeNTon();
            }

            return instance;
        }
    }
}