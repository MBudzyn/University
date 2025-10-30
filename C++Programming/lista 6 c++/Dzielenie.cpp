#include "Wyrazenie.h"
#include "Abs.h"
#include <math.h>
#include "Sin.h"
#include "Przeciwna.h"
#include "Odwrotna.h"
#include "Dodaj.h"
#include "Odejmij.h"
#include <stdexcept>

#include "Dzielenie.h"
string Dzielenie::zapis() {return "(" + lewa->zapis() + "/" + prawa->zapis() + ")";}
double Dzielenie::oblicz()
{
    double zmienna1 = lewa->oblicz();
    double zmienna2 = prawa->oblicz();
    if ( zmienna2 == 0 )
        throw invalid_argument("wrong value on input");
    return zmienna1 / zmienna2;
}
Dzielenie::Dzielenie(Wyrazenie *wskaznik1, Wyrazenie *wskaznik2) { lewa = wskaznik1; prawa = wskaznik2;}

