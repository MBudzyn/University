#include <stdexcept>
#include "Wyrazenie.h"
#include "Modulo.h"
string Modulo::zapis() {return "(" + lewa->zapis() + "%" + prawa->zapis() + ")";}
double Modulo::oblicz()
{
    double zmienna1 = lewa->oblicz();
    double zmienna2 = prawa->oblicz();
    if(zmienna1 != (int)zmienna1 or zmienna2 != (int)zmienna2)
        throw invalid_argument("wrong value on input");
    return lewa->oblicz() * (prawa->oblicz());
}
Modulo::Modulo(Wyrazenie *wskaznik1, Wyrazenie *wskaznik2) { lewa = wskaznik1; prawa = wskaznik2;}