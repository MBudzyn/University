function map(tab, f)
{
    var result = []
    for (let i=0; i<tab.length; i++)
    {
        result.push(f(tab[i]))
    }
    return result
}
function forEach(tab, f)
{
    for (let i=0; i<tab.length; i++)
    {
        f(tab[i])
    }
}
function filter(tab,condition)
{
    var result = []
    for (let i=0; i<tab.length; i++)
    {
        if (condition(tab[i]))
        {
            result.push(tab[i])
        }
    }
    return result
}

function increase_1(arg)
{
    return arg +1
}
console.log(map([1,2,3,4,5],x => x <5))

var a = [1,2,3,4]
forEach( a, _ => { console.log( _ ); } );
// [1,2,3,4]
console.log(filter( a, _ => _ < 3 ))
// [1,2]
console.log(map( a, _ => _ * 2 ))
// [2,4,6,8]
