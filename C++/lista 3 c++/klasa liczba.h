using namespace std;
#pragma once
// w publicznych  najpierw konstruktory
class liczba
{
private:
    double aktualna;
    int wskaznik;
    static int rozmiar;
    double* historia;
    int liczbael;

public:
    void ostatniahistoria ();
    void wypiszktualna();
    void nadajnowo(double a);
    liczba(double a);
    liczba();
    ~liczba();
    liczba(const liczba &t);
    liczba(liczba &&t);
    liczba& operator=(const liczba &t);
    liczba& operator=(liczba &&t);
};


