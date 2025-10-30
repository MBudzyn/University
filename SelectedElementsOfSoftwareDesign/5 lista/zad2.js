module.exports = {
    funkcjaA: funkcjaA
};

const modulB = require('./zad1.js');

function funkcjaA() {
    console.log('Funkcja z modułu A');
    modulB.funkcjaB();
}
