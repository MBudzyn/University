#pragma once

class Dodaj: public Wyrazenie {
private:
    Wyrazenie *lewa;
    Wyrazenie *prawa;
public:
    double oblicz();
    string zapis();
    Dodaj(Wyrazenie *jeden, Wyrazenie *dwa);

};
