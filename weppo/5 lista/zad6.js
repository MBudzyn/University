const fs = require('fs');
const readline = require('readline');

// Funkcja do analizy pliku logów i zliczania liczby żądań od poszczególnych adresów IP
function analyzeLog(filePath) {
  const clients = new Map(); // Mapa przechowująca adresy IP i liczbę żądań

  const readStream = fs.createReadStream(filePath);
  const rl = readline.createInterface({
    input: readStream,
    crlfDelay: Infinity
  });

  rl.on('line', (line) => {
    const ipAddress = line.split(' ')[1]; // Adres IP znajduje się na drugim miejscu w linii logu

    if (clients.has(ipAddress)) {
      clients.set(ipAddress, clients.get(ipAddress) + 1);
    } else {
      clients.set(ipAddress, 1);
    }
  });

  rl.on('close', () => {
    const sortedClients = [...clients.entries()].sort((a, b) => b[1] - a[1]);

    console.log('Najczęściej żądający klienci:');
    for (let i = 0; i < 3 && i < sortedClients.length; i++) {
      console.log(`${sortedClients[i][0]} ${sortedClients[i][1]}`);
    }
  });
}

// Analiza przykładowego pliku logów
const logFilePath = 'probnedane.txt'; // Zastąp ścieżką do własnego pliku logów
analyzeLog(logFilePath);
