var obiekt = { name: 'John', age: 30 };
var property = 'name';
console.log(obiekt[property])
console.log(obiekt.property) // -nie  mozna odwolac się np po zmiennej przechowującej nazwe property

var tablica = [1,2,3,4,5,5,6]
console.log(tablica["3"]) //jesli "liczba" to konwertowana na string jeśli o innego nic nie zwróci Nan

console.log( (![]+[])[+[]]+(![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]] ); //([["true"] + [][[]]])  trueandefinde
//             false[0]   +     false[1]  +   trueandefinde[10]       + false[2]
//4
//W podsumowaniu, typeof jest używany do określania typów pojedynczych wartości, 
//podczas gdy instanceof jest używany do sprawdzania,
//czy obiekt jest instancją konkretnej klasy.



tablica.length = 3
console.log(tablica.length)
tablica["koniec"] = "nie wiem"
console.log(tablica.length)
console.log(tablica)
console.log(tablica[obiekt])
tablica["koniec"] = "nie wiem"
console.log(tablica)
console.log(typeof(7))
