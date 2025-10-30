#include <iostream>
#include "Wyrazenie.h" //1
#include "Zmienna.h" //2
#include "Fi.h" //3
#include "Pi.h" //4
#include "E.h" //5
#include "Liczba.h" //6
#include "Abs.h" //7
#include "Sin.h" //8
#include "Cos.h" //9
#include "Ln.h" //10
#include "Exp.h" //11
#include "Przeciwna.h" //12
#include "Odwrotna.h" //13
#include "Dodaj.h" //14
#include "Odejmij.h" //15
#include "Mnozenie.h" //16
#include "Dzielenie.h" //17
#include "Potegowanie.h" //18
#include "Modulo.h" //19
#include "Logarytm.h" //20
using namespace std;

//zablokowanie tworzenia konstruktorów kopiujących ???!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
int main() {
    Zmienna kon = Zmienna("x");
    Wyrazenie *jeden1 = new Dzielenie
            ( new Mnozenie
                         (new Odejmij(
                                 new Zmienna("x") ,
                                  new Liczba(1)),
                          new Zmienna("x")),
            new Liczba(2));

    Wyrazenie *jeden2 = new Dzielenie(
                               new Dodaj(
                                         new Liczba(3),
                                          new Liczba(5)),
                               new Dodaj(
                                           new Liczba(2),
                                            new Mnozenie(
                                                    new Zmienna("x"),
                                                     new Liczba(7))));

    Wyrazenie *jeden3 = new Odejmij (
                             new Dodaj(
                                      new Liczba(2),
                                       new Mnozenie(
                                               new Zmienna("x"),
                                                new Liczba(7))),
                              new Dodaj (
                                      new Mnozenie(
                                              new Zmienna("y"),
                                               new Liczba(3)),
                                      new Liczba(5)));
   Wyrazenie *jeden4 = new Dzielenie(
                                    new Cos(
                                            new Mnozenie(
                                                 new Dodaj
                                                        (new Zmienna("x"), new Liczba(1)),
                                                 new Pi())),
                                    new Potegowanie(
                                            new E(),
                                            new Potegowanie(
                                                    new Zmienna("x"),
                                                    new Liczba(2))));



    Wyrazenie *pozostale = new Abs(
                                new Sin(
                                        new Logarytm(
                                                new Exp(
                                                        new Przeciwna(
                                                                new Fi()
                                                                )
                                                        ),
                                                new Odwrotna(
                                                        new Ln(
                                                            new Modulo(
                                                                new Liczba(3),
                                                                new Liczba(4)
                                                                )
                                                        )
                                                )
                                        )
            ));

    Pi jeden = Pi();
    Liczba dwa = Liczba(23);
    kon.wypisztab();
    cout<<endl;
    kon.dodaj(pair<string,double> ("y",7));
    kon.wypisztab();
    cout<<endl;
    kon.dodaj(pair<string,double> ("z",4));
    kon.zmienwartosc("x", 3);
    kon.wypisztab();
    cout<<endl;


    Zmienna testy =  Zmienna("x");
    testy.dodaj(pair<string,double> ("z",4));

    try{
        cout<<"zapis wyrazenia pierwszego a pod nim obliczona wartosc dla zmiennych z przedzialu <0;1>: "<<endl<<jeden1->zapis()<<endl;
        for(double i = 0; i<=100 ;i+=1)
        {

            testy.zmienwartosc("x", i/100);
            cout<<"x = "<<testy.zwrocwart("x")<<" -> "<<jeden1->oblicz()<<endl;
        }
        cout<<endl;
    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }
    try{
        cout<<"zapis wyrazenia drugiego a pod nim obliczona wartosc dla zmiennych z przedzialu <0;1>: "<<endl<<jeden2->zapis()<<endl;
        for(double i = 0; i<=100 ;i+=1)
        {

            testy.zmienwartosc("x", i/100);
            cout<<"x = "<<testy.zwrocwart("x")<<" -> "<<jeden1->oblicz()<<endl;
        }
        cout<<endl;
    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }
    try{
        cout<<"zapis wyrazenia trzeciego a pod nim obliczona wartosc dla zmiennej x z przedzialu <0;1> oraz y=0: "<<endl<<jeden3->zapis()<<endl;
        testy.zmienwartosc("y", 0);
        for(double i = 0; i<=100 ;i+=1)
        {
            testy.zmienwartosc("x", i/100);
            cout<<"x = "<<testy.zwrocwart("x")<<" y = 0 -> "<<jeden1->oblicz()<<endl;
        }
        cout<<endl;
    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }

    try{
        cout<<"zapis wyrazenia trzeciego a pod nim obliczona wartosc dla zmiennej x z przedzialu <0;1> oraz y=0.5: "<<endl<<jeden3->zapis()<<endl;

        testy.zmienwartosc("y", 0.5);
        for(double i = 0; i<=100 ;i+=1)
        {
            testy.zmienwartosc("x", i/100);

            cout<<"x = "<<testy.zwrocwart("x")<<" y = 1/2 -> "<<jeden1->oblicz()<<endl;
        }
        cout<<endl;
    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }

    try{
        cout<<"zapis wyrazenia trzeciego a pod nim obliczona wartosc dla zmiennej x z przedzialu <0;1> oraz y=1: "<<endl<<jeden3->zapis()<<endl;

        testy.zmienwartosc("y", 1);
        for(double i = 0; i<=100 ;i+=1)
        {
            testy.zmienwartosc("x", i/100);
            cout<<"x = "<<testy.zwrocwart("x")<<" y = 1 -> "<<jeden1->oblicz()<<endl;
        }
        cout<<endl;
    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }


    try{
        cout<<"zapis wyrazenia czwartego a pod nim obliczona wartosc dla zmiennych z przedzialu <0;1>: "<<endl<<jeden4->zapis()<<endl;
        for(double i = 0; i<=100 ;i+=1)
        {
            testy.zmienwartosc("x", i/100);
            cout<<"x = "<<testy.zwrocwart("x")<<" -> "<<jeden1->oblicz()<<endl;
        }
    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }
    try{
        cout<<endl;
        cout<<"zapis wyrazenia pozostalego a pod nim obliczona wartosc "<<endl;
        cout<<pozostale->zapis()<<endl;
        cout<<pozostale->oblicz()<<endl;
    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }
//-----------------------------
    try{
        cout<<endl;
        cout<<jeden1->zapis()<<" x = 0 y = 0 ->"<<jeden1->oblicz()<<endl;
        cout<<jeden2->zapis()<<" x = 0 y = 0 ->"<<jeden2->oblicz()<<endl;
        cout<<jeden3->zapis()<<" x = 0 y = 0 ->"<<jeden3->oblicz()<<endl;
        cout<<jeden4->zapis()<<" x = 0 y = 0 ->"<<jeden4->oblicz()<<endl;
        cout<<endl;
        cout<<jeden1->zapis()<<" x = 0 y = 0.5 ->"<<jeden1->oblicz()<<endl;
        cout<<jeden2->zapis()<<" x = 0 y = 0.5 ->"<<jeden2->oblicz()<<endl;
        cout<<jeden3->zapis()<<" x = 0 y = 0.5 ->"<<jeden3->oblicz()<<endl;
        cout<<jeden4->zapis()<<" x = 0 y = 0.5 ->"<<jeden4->oblicz()<<endl;
        cout<<endl;
        cout<<jeden1->zapis()<<" x = 0.5 y = 0 ->"<<jeden1->oblicz()<<endl;
        cout<<jeden2->zapis()<<" x = 0.5 y = 0 ->"<<jeden2->oblicz()<<endl;
        cout<<jeden3->zapis()<<" x = 0.5 y = 0 ->"<<jeden3->oblicz()<<endl;
        cout<<jeden4->zapis()<<" x = 0.5 y = 0 ->"<<jeden4->oblicz()<<endl;
        cout<<endl;
        cout<<jeden1->zapis()<<" x = 0.5 y = 0.5 ->"<<jeden1->oblicz()<<endl;
        cout<<jeden2->zapis()<<" x = 0.5 y = 0.5 ->"<<jeden2->oblicz()<<endl;
        cout<<jeden3->zapis()<<" x = 0.5 y = 0.5 ->"<<jeden3->oblicz()<<endl;
        cout<<jeden4->zapis()<<" x = 0.5 y = 0.5 ->"<<jeden4->oblicz()<<endl;
        cout<<endl;
        cout<<jeden1->zapis()<<" x = 1 y = 1 ->"<<jeden1->oblicz()<<endl;
        cout<<jeden2->zapis()<<" x = 1 y = 1 ->"<<jeden2->oblicz()<<endl;
        cout<<jeden3->zapis()<<" x = 1 y = 1 ->"<<jeden3->oblicz()<<endl;
        cout<<jeden4->zapis()<<" x = 1 y = 1 ->"<<jeden4->oblicz()<<endl;

    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }
    //--------------------------------



    return 0;
}
