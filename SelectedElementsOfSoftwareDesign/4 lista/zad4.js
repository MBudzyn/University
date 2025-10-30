var n = 1;
// liczba ma prototyp?
console.log( typeof Object.getPrototypeOf( n ) );
// można jej dopisać pole/funkcję?
n.foo = 'foo';
console.log( n.foo );

//W rzeczywistości, ta linia kodu próbuje uzyskać dostęp do prototypu wartości prymitywnej, 
//ale w wyniku zwrócony jest obiekt prototypowy o nazwie Number. To jest wewnętrzny obiekt prototypowy,
// który jest używany w języku JavaScript dla typu prymitywnego number.
// Nie oznacza to, że wartości typów prostych same w sobie mają prototypy, na których możesz definiować pola i metody.
