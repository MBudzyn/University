function fiborek(num) {
    if (num == 0) {
        return 0;
    }
    if (num == 1) {
        return 1;
    }
    else {
        return fiborek(num - 1) + fiborek(num - 2);
    }
}
function memoize(fn) {
    var cache = {};
    return function (n) {
        if (n in cache) {
            return cache[n];
        }
        else {
            var result = fn(n);
            cache[n] = result;
            return result;
        }
    };
}
var fiborekt = memoize(fiborek);
console.log(fiborekt(20));
