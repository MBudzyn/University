using namespace std;
#include "kolor.h"
#include<iostream>
#include<cmath>
#include "Piksel.h"
#include <stdexcept>

Kolor::Kolor(int r,int g ,int b)
{
    if (r > 255 or r < 0 or g > 255 or g < 0 or b > 255 or b < 0) {
        throw invalid_argument("wrong value");
    }
    this->R = r;
    this->G = g;
    this->B = b;
}
Kolor::Kolor(){ this->R = 0; this->G = 0; this->B = 0; }
Kolorprzezroczysty::Kolorprzezroczysty(int alfa){this->alfa = alfa;}
Kolorprzezroczysty::Kolorprzezroczysty() {this->alfa = 0;}
Kolornazwany::Kolornazwany(string nazwa)
{
    for(int i = 0;i< nazwa.length();i++)
    {

        char zmienna = nazwa[i];
        int nowa = static_cast<int>(zmienna);
        if (nowa > 122 or nowa < 97)
            throw invalid_argument("wrong value");
    }
    this->nazwa = nazwa;

}
Kolornazwany::Kolornazwany() {this->nazwa = "";}

void Kolor::setR( int r)
{
    if (r > 255 or r < 0 )
        throw invalid_argument("wrong value");
    this->R = r;
}
void Kolor::setG(int g)
{
    if (g > 255 or g < 0 )
        throw invalid_argument("wrong value");
    this->G = g;
}
void Kolor::setB(int b)
{
    if (b > 255 or b < 0)
        throw invalid_argument("wrong value");
    this->B = b;}

int Kolor::getR()  {return R;}
int Kolor::getG() {return G;}
int Kolor::getB()  {return B;}

void Kolor::przyciemnij(int procent)
{
    if (procent > 100 or procent < 0)
        throw invalid_argument("wrong value");
    R = round((R - R * procent/100));
    G = round((G - G * procent/100));
    B = round((B - B * procent/100));
}
void Kolor::rozjasnij(int procent)
{

    *this = Kolor(round((R + R * procent/100)), round((G + G * procent/100)), round((B + B * procent/100)));
}
void Kolor::wypiszwszystkie(){cout<<"dane danego koloru w postaci R G B to : "<<(int)R<<" "<<(int)G<<" "<<(int)B<<endl;}

