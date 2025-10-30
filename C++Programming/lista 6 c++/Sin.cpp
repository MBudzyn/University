#include "Wyrazenie.h"
#include "Abs.h"
#include <math.h>
#include "Sin.h"

string Sin::zapis() {return "Sin(" + srodek->zapis() + ")";}
double Sin::oblicz() {return sin(srodek->oblicz());}
Sin::Sin(Wyrazenie *wskaznik) { srodek = wskaznik;}