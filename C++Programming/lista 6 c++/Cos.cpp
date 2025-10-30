#include "Wyrazenie.h"
#include "Cos.h"
#include "Abs.h"
#include <math.h>
#include "Sin.h"

string Cos::zapis() {return "cos(" + srodek->zapis() + ")";}
double Cos::oblicz() {return cos(srodek->oblicz());}
Cos::Cos(Wyrazenie *wskaznik) { srodek = wskaznik;}