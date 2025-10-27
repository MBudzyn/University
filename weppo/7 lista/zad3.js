var http = require('http');
var server =
 http.createServer(
 (req, res) => {
 res.end(`hello world ${new Date()}`);
 });

const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.set('view engine', 'ejs'); // Ustawienie silnika szablonów EJS

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public')); // Ustawienie folderu publicznego dla plików statycznych (np. CSS)

// Dane tymczasowe przechowujące zgłoszenia
let submissions = [];

// Strona główna - formularz zgłoszenia
app.get('/', (req, res) => {
  res.render('form', { error: null });
});

// Obsługa przesłania formularza zgłoszenia
app.post('/submit', (req, res) => {
  const { firstName, lastName, occupation, tasks } = req.body;

  // Sprawdzenie czy pola imienia, nazwiska i zajęć są wypełnione
  if (!firstName || !lastName || !occupation) {
    res.render('form', { error: 'Proszę wypełnić wszystkie pola!' });
  } else {
    // Tworzenie nowego zgłoszenia i dodawanie go do listy zgłoszeń
    const newSubmission = {
      firstName,
      lastName,
      occupation,
      tasks: []
    };

    // Pobieranie danych dotyczących zadań
    for (let i = 1; i <= 10; i++) {
      const taskName = `task${i}`;
      const taskScore = parseInt(req.body[taskName]) || 0; // Jeśli brak wartości, przyjmujemy 0

      newSubmission.tasks.push({
        name: taskName,
        score: taskScore
      });
    }

    submissions.push(newSubmission);

    // Przekierowanie do widoku wydruku
    res.redirect(`/print/${submissions.length - 1}`);
  }
});

// Strona wydruku - pasek zgłoszenia
app.get('/print/:id', (req, res) => {
  const id = req.params.id;
  const submission = submissions[id];

  if (!submission) {
    res.send('Nie znaleziono zgłoszenia');
  } else {
    res.render('print', { submission });
  }
});

// Nasłuchiwanie na porcie 3001
app.listen(3001, () => {
  console.log('Aplikacja działa na porcie 3001');
});