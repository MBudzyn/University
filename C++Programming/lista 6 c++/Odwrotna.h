#pragma once

class Odwrotna: public Wyrazenie {
private:
    Wyrazenie *srodek;
public:
    double oblicz() override;
    string zapis() override;
    Odwrotna(Wyrazenie *jeden);

};
