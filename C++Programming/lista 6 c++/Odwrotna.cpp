#include "Wyrazenie.h"
#include "Abs.h"
#include <math.h>
#include "Sin.h"
#include "Przeciwna.h"
#include "Odwrotna.h"
#include <stdexcept>
string Odwrotna::zapis() {return "(" + srodek->zapis() + ")";}
double Odwrotna::oblicz()
{
    double zmienna1 = srodek->oblicz();
    if ( zmienna1 == 0 )
        throw invalid_argument("nie istnieje liczba odwrotna do zera");
    return 1/(zmienna1);
}
Odwrotna::Odwrotna(Wyrazenie *wskaznik) { srodek = wskaznik;}

