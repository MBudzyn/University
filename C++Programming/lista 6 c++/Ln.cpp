#include "Wyrazenie.h"
#include <math.h>
#include "Ln.h"
string Ln::zapis() {return "Ln(" + srodek->zapis() + ")";}
double Ln::oblicz() {return log(srodek->oblicz());}
Ln::Ln(Wyrazenie *wskaznik) { srodek = wskaznik;}

