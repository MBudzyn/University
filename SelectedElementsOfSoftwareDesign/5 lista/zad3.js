const stdin = process.stdin;
const random_number = Math.floor(Math.random() * 100) + 1;
//readline
console.log("select number from 1 to 100")
stdin.on("data", function(d) {

    if (d == random_number)
    {
        console.log("gratulation, you won!!!")
        process.exit();
    }
    else if (d < random_number)
    {
        console.log("my number is grater than yours")
    }
    else 
    {
        console.log("my number is smaller than yours")
    }

});

