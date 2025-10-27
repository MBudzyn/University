const fs = require('fs');
const http = require('http');

(async function () {
  try {
    const privateKey = fs.readFileSync('key1.key', 'utf8'); // Wczytanie klucza prywatnego
    const certificate = fs.readFileSync('certyfikat.crt', 'utf8'); // Wczytanie certyfikatu .crt
    const credentials = { key: privateKey, cert: certificate }; // Konfiguracja klucza i certyfikatu

    const server = http.createServer(credentials, (req, res) => {
      res.setHeader('Content-type', 'text/html; charset=utf-8');
      res.end(`hello world ${new Date()}`);
    });

    server.listen(3000);
    console.log('started');
  } catch (err) {
    console.error('Błąd wczytywania plików certyfikatu lub klucza prywatnego:', err);
  }
})();
