#pragma once

class Odejmij: public Wyrazenie {
private:
    Wyrazenie *lewa;
    Wyrazenie *prawa;
public:
    double oblicz() override;
    string zapis() override;
    Odejmij(Wyrazenie *jeden, Wyrazenie *dwa);

};