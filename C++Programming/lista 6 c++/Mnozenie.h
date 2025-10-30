#pragma once

class Mnozenie: public Wyrazenie {
private:
    Wyrazenie *lewa;
    Wyrazenie *prawa;
public:
    double oblicz() override;
    string zapis() override;
    Mnozenie(Wyrazenie *jeden, Wyrazenie *dwa);

};