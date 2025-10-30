
function pierwsze(){
    result = [2]
    for (let i = 3; i < 100000; i++)
    {
        var condition = true
        for(let j = 2;j<i;j++)
        {
            if(i%j==0)
            {
                condition = false
            }
            
        }
        if (condition)
        {
            result.push(i)
        }

        
    }
    return result;
}
console.log(pierwsze())

