#include "Wyrazenie.h"
#include "Abs.h"
#include <math.h>
#include "Sin.h"
#include "Przeciwna.h"
#include "Odwrotna.h"
#include "Dodaj.h"
string Dodaj::zapis() {return "(" + lewa->zapis() + "+" + prawa->zapis() + ")";}
double Dodaj::oblicz() {return lewa->oblicz() + (prawa->oblicz());}
Dodaj::Dodaj(Wyrazenie *wskaznik1, Wyrazenie *wskaznik2) { lewa = wskaznik1; prawa = wskaznik2;}

