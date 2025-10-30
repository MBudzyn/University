#include "Wyrazenie.h"
#include "Odejmij.h"
string Odejmij::zapis() {return "(" + lewa->zapis() + "-" + prawa->zapis() + ")";}
double Odejmij::oblicz() {return lewa->oblicz() - (prawa->oblicz());}
Odejmij::Odejmij(Wyrazenie *wskaznik1, Wyrazenie *wskaznik2) { lewa = wskaznik1; prawa = wskaznik2;}

