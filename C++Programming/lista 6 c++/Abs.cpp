#include "Wyrazenie.h"
#include "Abs.h"
#include <math.h>

string Abs::zapis() {return "(" + srodek->zapis() + ")";}
double Abs::oblicz() {return abs(srodek->oblicz());}
Abs::Abs(Wyrazenie *wskaznik) { srodek = wskaznik;}