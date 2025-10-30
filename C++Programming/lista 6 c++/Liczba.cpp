#include "Wyrazenie.h"
#include "Zmienna.h"
#include "Liczba.h"

Liczba::Liczba(double wartosc) {liczba = wartosc;}

double Liczba::oblicz() {return liczba;}
string Liczba::zapis() {return to_string(liczba);}