var personProto = {
    say: function() {
    return this.name;
    }
   }
   var p3 = {
    second_name : "Natan",
    make: function() {
        return this.second_name + " is making cake";
    },
    make_fun: function()
    {
        return this.second_name + " is having fun"
    }
   }
   var p1 = {
    name: 'jan'
   }
   Object.setPrototypeOf( p1, personProto );
   var p2 = {
    name: 'tomasz'
   }
   Object.setPrototypeOf( p2, personProto );
   console.log( p1.say() );
   console.log( p2.say() );
   
   function getLastProto(o) {
    var p = o;
    do {
    o = p;
    p = Object.getPrototypeOf(o);
    } while (p);
    return o;
   }

  console.log(getLastProto(p1))
  console.log(getLastProto(p2))
  console.log(getLastProto(p3))