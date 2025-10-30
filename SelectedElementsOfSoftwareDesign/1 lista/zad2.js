function div(a, b){
    return (Math.round(a/b - 0.5))
  }

function sum_of_digits(number1){
    result1 = 0;
    
    while (number1 > 0)
    {
        result1 += number1 %10;
        number1 = div(number1 ,10);
    }
    return result1;
}

function digits(number2){
    result2 = [];
    
  
    while (number2 > 0)
    {
        result2.push(number2%10);
        number2 = div(number2,10);
    }
    return result2;
}



function naturalne(){
    result = []
    for (let i = 1; i < 100000; i++)
    {
        var pom = 0;
        var pom2 = 0;
        sum = sum_of_digits(i)
        if (i%sum != 0)
        {
            pom = 1
        }
        var table_of_digits = digits(i);
        for (let j = 0; j<table_of_digits.length;j++)
        {
            if (i%table_of_digits[j]!=0)
            {
                pom2++;
            };
        }
        if (pom2 == 0 && pom == 0)
        {
            result.push(i);
        }
        
    }
    return result;
}


console.log(naturalne())