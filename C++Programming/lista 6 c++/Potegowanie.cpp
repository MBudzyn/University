#include <stdexcept>
#include "Wyrazenie.h"
#include "Potegowanie.h"
#include <math.h>
string Potegowanie::zapis() {return "(" + lewa->zapis() + "^" + prawa->zapis() + ")";}
double Potegowanie::oblicz()
{
    double zmienna1 = lewa->oblicz();
    double zmienna2 = prawa->oblicz();
    if ( zmienna1 < 0 and (int)zmienna2 != zmienna2)
        throw invalid_argument("wrong value on input");
    return pow(zmienna1 , zmienna2);
}
Potegowanie::Potegowanie(Wyrazenie *wskaznik1, Wyrazenie *wskaznik2) { lewa = wskaznik1; prawa = wskaznik2;}

