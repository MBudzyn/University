function* createGenerator() {
    var z1 = 0
    var z2 = 1
    yield 0
    yield 1
    while (true)
    {
            yield z2 + z1
            z2 = z1 + z2 
            z1 = z2 - z1
        
    }
   }
   //it = createGenerator();
   //for ( var _res; _res = it.next(), !_res.done; ) {
    //console.log( _res.value );
   //}
   //var bar = {//dla generatora dziala
   // [Symbol.iterator]: createGenerator
   //}
  // for ( var b of bar ) {
   // console.log( b );
  // }

  function createFibonacciGenerator() {
        var _state = 0;
        var _state2 = 1;
        return {
            next: function() {
                var current = _state;
                var nextFib = _state + _state2;
                _state = _state2;
                _state2 = nextFib;
                return {
                    value: current,
                    done: false 
                }
            }
        };
    }


var fibonacciGenerator = createFibonacciGenerator();

for (var i = 0; i < 10; i++) {
        var result = fibonacciGenerator.next();
        console.log(result.value);
        }

var bar = {
    [Symbol.iterator]: createFibonacciGenerator //dla generatora tez dziala
   }
  for ( var b of bar ) {
    console.log( b );
  }