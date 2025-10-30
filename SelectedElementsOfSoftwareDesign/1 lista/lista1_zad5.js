function fiborek(number)
{

    if (number == 0){ return 0 }
    if (number == 1){ return 1 }
    else 
    {
        return fiborek(number-1) + fiborek(number-2)
    }
}
function fiboiter(number)
{
    var pom1 = 0
    var pom2 = 1
    if (number == 0){ return 0 }
    if (number == 1){ return 1 }
    for (let i=1; i<number; i++)
    {
        pom2 = pom1 + pom2
        pom1 = pom2 - pom1
    }
    return pom2
}

function mesure(func, n) {

    console.time(n);
    func(n)
    console.timeEnd(n);
}

for(let i = 10; i<30; i++)
{
    mesure(fiboiter, i)
}

for(let i = 10; i<30; i++)
{
    mesure(fiborek, i)
}
