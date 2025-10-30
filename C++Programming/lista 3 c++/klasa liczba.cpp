#include<iostream>
#include "klasa liczba.h"
using namespace std;


int liczba::rozmiar = 3;

liczba::liczba(double a)
{
    historia = new double [ rozmiar ];
    wskaznik = 0;
    aktualna = a;
    historia[ wskaznik ] = a;
    liczbael = 0;
}

liczba::liczba()
{
    historia = new double [ rozmiar ];
    wskaznik = 0;
    aktualna = 0;
    historia[ wskaznik ] = 0;
    liczbael = 0;
}

liczba::~liczba()
{
    delete[] historia;
}

liczba::liczba(const liczba &t)
{
    this->wskaznik = 0;
    this->historia = new double [rozmiar];
    this->historia[0] = t.aktualna;
    this->aktualna = t.aktualna;
    this->liczbael = 1;
}

liczba& liczba::operator=(const liczba &t)
{
    this->wskaznik = 0;
    this->historia = new double [rozmiar];
    this->historia[0] = t.aktualna;
    this->aktualna = t.aktualna;
    this->liczbael = 1;
    return *this;
}

liczba::liczba(liczba &&t)
    :historia(t.historia), wskaznik(t.wskaznik), aktualna(t.aktualna), liczbael(t.liczbael)
{
   t.wskaznik = 0;
   t.historia = nullptr;
   t.liczbael = 0;
   t.aktualna = 0;

}

liczba& liczba::operator=(liczba &&t)
{
    wskaznik = t.wskaznik ;
    historia = t.historia;
    liczbael = t.liczbael;
    aktualna = t.aktualna;
    return *this;
}

void liczba::ostatniahistoria()
{
    if( liczbael != 1 )
    {
        historia[ wskaznik ] = 0;
        if ( wskaznik != 0 )
            { wskaznik -= 1; }
        else
            { wskaznik = rozmiar -1; }
        aktualna = historia[ wskaznik ];
        liczbael -= 1;
    }
}

void liczba::nadajnowo(double a)
{
    wskaznik = ( wskaznik + 1 ) % rozmiar;
    historia[ wskaznik]  = a;
    aktualna = a;
    liczbael += 1;
}

void liczba::wypiszktualna() {cout<<"aktualna wartosc liczby to: "<<aktualna<<endl;}