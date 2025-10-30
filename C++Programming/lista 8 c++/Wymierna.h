#pragma once
#include <iostream>
namespace obliczenia {
    class Wymierna {

        int licznik, mianownik;
    public:
        int getlicznik() const;

        int getmianownik() const;

        Wymierna(int, int);

        explicit Wymierna(int);

        Wymierna();

        Wymierna operator+(const Wymierna& other) const;
        Wymierna operator-(const Wymierna& other) const;
        Wymierna operator*(const Wymierna& other) const;
        Wymierna operator/(const Wymierna& other) const;
        Wymierna operator!() const;
        Wymierna operator-() const;
        explicit operator  int() const;
        explicit operator double() const;

        friend std::ostream& operator<< (std::ostream &wyj, const Wymierna &w);




    };
}
