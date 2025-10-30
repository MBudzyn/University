#pragma once

class Dzielenie: public Wyrazenie {
private:
    Wyrazenie *lewa;
    Wyrazenie *prawa;
public:
    double oblicz() override;
    string zapis() override;
    Dzielenie(Wyrazenie *jeden, Wyrazenie *dwa);

};