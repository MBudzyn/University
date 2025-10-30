#include "Wyrazenie.h"
#include "Zmienna.h"

vector<pair<string, double>> Zmienna::tablica;

void Zmienna::dodaj(pair<string, double> zmienna)
{

    int w =0;
    obecna = zmienna.first;
    for (int i =0; i<tablica.size(); i++)
    {
        if( tablica[i].first == zmienna.first)
            w ++;
    }
    if (w == 0)
        tablica.push_back(zmienna);

}
void Zmienna::zmienwartosc(string nazwa, double nowa)
{
    for(int i=0; i<tablica.size();i++)
        if (tablica[i].first == nazwa)
        {
            tablica[i].second = nowa;

        }

}
double Zmienna::zwrocwart(string nazwa)
{
    for(int i=0; i<tablica.size();i++)
        if (tablica[i].first == nazwa)
        {
            return tablica[i].second;
        }

}

void Zmienna::usun(string nazwa) {
    for (int i = tablica.size() - 1; i >= 0; i--) {
        if (tablica[i].first == nazwa) {
            tablica.erase(tablica.begin() + i);
        }
    }
}
Zmienna::Zmienna(string nazwa)
{
    int w =0;
    obecna = nazwa;
    for (int i =0; i<tablica.size(); i++)
        {
      if( tablica[i].first == nazwa)
          w ++;
        }
    if (w == 0)
        tablica.push_back(pair<string ,double>(nazwa, 0));
}

void Zmienna::wypisztab()
{
    for(int i=0; i<tablica.size(); i++)
    {cout<<"zmienna o nazwie: "<<tablica[i].first<<" przechowuje wartosc: "<<tablica[i].second<<endl;}
}

double Zmienna::oblicz()
{
    for (int i=0; i<tablica.size();i++)
        if(obecna == tablica[i].first)
            return tablica[i].second;

}
string Zmienna::zapis() {return obecna;}

