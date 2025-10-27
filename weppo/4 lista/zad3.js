var Person = function(name, surname) {
    this.name = name;
    this.surname = surname;
   }
   Person.prototype.say = function() {
    return `${this.name} ${this.surname}`;
   }

var p = new Person('jan', 'kowalski');
console.log( p.say() );

var Worker = function(name, surname, age) {
    // wywołanie bazowej funkcji konstruktorowej
    Person.call( this, name, surname );
    this.age = age;
   }
   // powiązanie łańcucha prototypów
   Worker.prototype = Object.create( Person.prototype );
   Worker.prototype.say = function() {
    // "wywołanie metody z klasy bazowej"
    var _ = Person.prototype.say.call( this );
    return `${_} ${this.age}`;
   }
   var w = new Worker('jan', 'kowalski', 48);
   console.log( w.say() );

//Worker.prototype = Person.prototype; - W tym przypadku wszystkie instancje obu klas będą 
//dzieliły ten sam prototyp, co może prowadzić do nieoczekiwanych błędów i konfliktów w przypadku modyfikacji prototypu.

//Worker.prototype = new Person(); - W tym przypadku Worker.prototype jest instancją obiektu Person, 
//co prowadzi do tworzenia nowego obiektu prototypowego na podstawie Person. Jednak to podejście
//Zwiększa zużycia pamięci - Każda instancja Worker dziedziczy całą strukturę prototypową Person, 
//co może prowadzić do zwiększonego zużycia pamięci w przypadku bardziej skomplikowanych obiektów.

//Worker.prototype = Object.create(Person.prototype); - To podejście rozwiązuje powyższe problemy. 
//Metoda Object.create(Person.prototype) tworzy nowy obiekt, który jest prototypem Worker. 
//Ten obiekt dziedziczy prototyp Person bez wywoływania konstruktora Person i bez współdzielenia prototypu z Person.
// Dzięki temu możemy uniknąć konfliktów i zmian w prototypie Person podczas modyfikacji prototypu Worker