function fiborekstary(number)
{

    if (number == 0){ return 0 }
    if (number == 1){ return 1 }
    else 
    {
        return fiborekstary(number-1) + fiborekstary(number-2)
    }
}
function fiborek(number)
{

    if (number == 0){ return 0 }
    if (number == 1){ return 1 }
    else 
    {
        return fiborek(number-1) + fiborek(number-2)
    }
}
   function memoize(fn) {
    var cache = {};
    return function(n) {
    if ( n in cache ) {
    return cache[n]
    } else {
    var result = fn(n);
    cache[n] = result;
    return result;
    }
    }
   }
   var fiborek = memoize(fiborek);

   function mesure(func, n) {

    console.time(n);
    func(n)
    console.timeEnd(n);
}

for(let i = 40; i>2; i--)
{
    mesure(fiborekstary, i)
}

for(let i = 40; i>2; i--)
{
    mesure(memofac2, i)
}