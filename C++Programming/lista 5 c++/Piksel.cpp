using namespace std;
#include "kolor.h"
#include<iostream>
#include<cmath>
#include "Piksel.h"


Piksel::Piksel() {this->x = 0; this->y = 0;}
Piksel::Piksel(int x,int y)
{
    if(x>maksxekran or x<0 or y>maksyekran or y<0)
        throw invalid_argument("wrong value");
    this->x = x; this->y = y;

}
Pikselkolorowy::Pikselkolorowy() {kolor = Kolornt();}
//cout<<"wsp y danego piksela to: "<<y<<endl;
//cout<<"wsp x danego piksela to: "<<x<<endl;
int Piksel::getx() { return x;}
int Piksel::gety() { return y;}

int Piksel::odlegloscdol() {cout<<"odleglosc do dolu: "<<y<<endl; return y;}
int Piksel::odlegloscgora() {cout<<"odleglosc do gory: "<<maksyekran-y<<endl; return maksyekran - y;}
int Piksel::odlegloscprawy() {cout<<"odleglosc do prawej: "<<maksxekran-x<<endl; return maksxekran -x;}
int Piksel::odleglosclewy() {cout<<"odleglosc do lewej: "<<x<<endl; return x;}
void Pikselkolorowy::przesunovector(int xmove, int ymove)
{
    if(x+xmove < 0 or x+xmove > maksxekran or y+ymove > maksyekran or y+ymove < 0)
        throw invalid_argument("wrong value");
    x +=xmove;
    y +=ymove;
}



int distance(Piksel *pixel1, Piksel *pixel2)
{
    return int(round(sqrt(pow(pixel1->getx() - pixel2->getx(), 2) + pow(pixel1->gety() - pixel2->gety(), 2))));
}