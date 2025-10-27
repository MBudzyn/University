function createGenerator(limit) 
{
    var _state = 0;
    return function() { // zwrocenie funkcji 
            return {
            next : function() 
                    {
            return {
                value : _state,
                done : _state++ >= limit
                }
            }
        }
        }
    }
    

var foo = 
    {
    [Symbol.iterator] : createGenerator(20)
    };

    var foo2 = 
    {
    [Symbol.iterator] : createGenerator(25)
    };

    var foo3 = 
    {
    [Symbol.iterator] : createGenerator(30)
    };

    var foo4 = 
    {
    [Symbol.iterator] : createGenerator(40)
    };

 for ( var f of foo )
    console.log(f);
    
for ( var f of foo2 )
    console.log(f);

for ( var f of foo3 )
    console.log(f);

for ( var f of foo4 )
    console.log(f);