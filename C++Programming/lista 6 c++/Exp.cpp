#include "Wyrazenie.h"
#include "Exp.h"
#include "Cos.h"
#include "Abs.h"
#include <math.h>
#include "Sin.h"

string Exp::zapis() {return "exp(" + srodek->zapis() + ")";}
double Exp::oblicz() {return exp(srodek->oblicz());}
Exp::Exp(Wyrazenie *wskaznik) { srodek = wskaznik;}