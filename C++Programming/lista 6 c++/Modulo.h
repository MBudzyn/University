#pragma once

class Modulo: public Wyrazenie {
private:
    Wyrazenie *lewa;
    Wyrazenie *prawa;
public:
    double oblicz() override;
    string zapis() override;
    Modulo(Wyrazenie *jeden, Wyrazenie *dwa);

};