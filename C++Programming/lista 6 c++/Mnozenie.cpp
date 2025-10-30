
#include "Wyrazenie.h"
#include "Mnozenie.h"
string Mnozenie::zapis() {return "(" + lewa->zapis() + "*" + prawa->zapis() + ")";}
double Mnozenie::oblicz() {return lewa->oblicz() * (prawa->oblicz());}
Mnozenie::Mnozenie(Wyrazenie *wskaznik1, Wyrazenie *wskaznik2) { lewa = wskaznik1; prawa = wskaznik2;}

