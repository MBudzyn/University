#include "Wyrazenie.h"
#include <math.h>
#include "Logarytm.h"
#include <stdexcept>
string Logarytm::zapis() {return "log(" + lewa->zapis() + ") " + " (" + prawa->zapis() + ")";}
double Logarytm::oblicz()
{
    double zmienna1 = lewa->oblicz();
    double zmienna2 = prawa->oblicz();
    if ( zmienna1 <= 0 or zmienna2 <= 0 or zmienna1 == 1)
        throw invalid_argument("wrong value on input");

    return log(zmienna1/ zmienna2);
}
Logarytm::Logarytm(Wyrazenie *wskaznik1, Wyrazenie *wskaznik2) { lewa = wskaznik1; prawa = wskaznik2;}

