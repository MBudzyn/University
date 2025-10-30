#pragma once

class Przeciwna: public Wyrazenie {
private:
    Wyrazenie *srodek;
public:
    double oblicz() override;
    string zapis() override;
    Przeciwna(Wyrazenie *jeden);

};
