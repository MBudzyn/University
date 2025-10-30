#include "Wyjdziel0.h"
#include "Wymierna.h"
#include "Wyjprzekzak.h"
#include <cmath>
#include <numeric>
#include <string>
#include <unordered_map>
#include <climits>
using namespace std;
using namespace obliczenia;



string okresowa(int licznik, int mianownik) {
    if (licznik == 0) {
        return "0";
    }
    string res = "";
    if (licznik < 0 ^ mianownik < 0) //ksor zwraca wartosc true wtedy gdy jeden z warunkuch jest spoelnion a drugi nie
    {
        res += "-";
    }
    long long n = abs((long long)licznik);
    long long d = abs((long long)mianownik);
    res += to_string(n / d);
    long long r = n % d;
    if (r == 0) {
        return res;
    }
    res += ".";
    unordered_map<long long, int> map;
    while (r != 0) {
        if (map.find(r) != map.end()) {
            res.insert(map[r], 1, '(');
            res += ")";
            break;
        }
        map[r] = res.size();
        r *= 10;
        res += to_string(r / d);
        r %= d;
    }
    return res;
}


ostream& obliczenia::operator<<(std::ostream& wyj, const Wymierna& w)
{
    wyj << okresowa(w.licznik, w.mianownik);

    return wyj;
}

int Wymierna::getlicznik() const {return licznik;}

int Wymierna::getmianownik() const {return mianownik;}

Wymierna ::Wymierna(int licz, int mian)
{
    if (mian == 0){ throw Wyjdziel0("nie mozna dzielic przez zero"); }

    if (mian < 0){licz = -licz ; mian = -mian;}

    int gcd = std::gcd(abs(licz),abs(mian));
    licz /=gcd;

    mian /=gcd;

    licznik = licz ;

    mianownik = mian ;
}
Wymierna::Wymierna(int licz) : Wymierna (licz ,1){}
Wymierna::Wymierna() {licznik = 0; mianownik = 1;}

Wymierna Wymierna::operator+(const Wymierna &other) const
{
    Wymierna wynik;
    int l,m;
    if ((long long int)getlicznik() * other.getmianownik() + getmianownik()* other.getlicznik() > INT_MAX
        or (long long int)getmianownik() * other.getmianownik() > INT_MAX)
        throw Wyjprzekzak("przkroczony zakres int");

    l = getlicznik() * other.getmianownik() + getmianownik()* other.getlicznik();
    m = getmianownik() * other.getmianownik();
    wynik = Wymierna(l,m);
    return wynik;
}
Wymierna Wymierna::operator-(const Wymierna &other) const
{
    Wymierna wynik;
    int l,m;
    if ((long long int)getlicznik() * other.getmianownik() - getmianownik()* other.getlicznik() > INT_MAX
    or (long long int)getmianownik() * other.getmianownik() > INT_MAX)
        throw Wyjprzekzak("przkroczony zakres int");

    l = getlicznik() * other.getmianownik() - getmianownik()* other.getlicznik();
    m = getmianownik() * other.getmianownik();
    wynik = Wymierna(l,m);
    return wynik;
}
Wymierna Wymierna::operator*(const Wymierna &other) const
{
    Wymierna wynik;
    int l,m;
    if ((long long int)getlicznik() * other.getlicznik() > INT_MAX or getmianownik() * other.getmianownik() > INT_MAX)
        throw Wyjprzekzak("przkroczony zakres int");
    l = getlicznik() *  other.getlicznik();
    m = getmianownik() * other.getmianownik();
    wynik = Wymierna(l,m);
    return wynik;
}
Wymierna Wymierna::operator/(const Wymierna &other) const
{
    Wymierna wynik;
    int l,m;
    if ((long long int)getlicznik() * other.getmianownik() > INT_MAX or (long long int)getmianownik() * other.getlicznik() > INT_MAX)
        throw Wyjprzekzak("przkroczony zakres int");

    l = getlicznik() * other.getmianownik();
    m = getmianownik() * other.getlicznik();
    wynik = Wymierna(l,m);
    return wynik;
}
Wymierna Wymierna::operator-() const { return {-getlicznik(), getmianownik()};}
Wymierna Wymierna::operator!() const { return {getmianownik(),getlicznik()};}
Wymierna::operator double() const
{
    double wynik = (double)getlicznik()/(double)getmianownik();
    return wynik;
}

Wymierna::operator int() const {return round(double(*this));}

