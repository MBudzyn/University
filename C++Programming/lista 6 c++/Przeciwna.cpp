#include "Wyrazenie.h"
#include "Abs.h"
#include <math.h>
#include "Sin.h"
#include "Przeciwna.h"
string Przeciwna::zapis() {return "(" + srodek->zapis() + ")";}
double Przeciwna::oblicz() {return -1*(srodek->oblicz());}
Przeciwna::Przeciwna(Wyrazenie *wskaznik) { srodek = wskaznik;}

