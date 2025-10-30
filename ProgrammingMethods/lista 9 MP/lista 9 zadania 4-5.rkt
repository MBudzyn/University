#lang racket
;----------------------------------------------deklaracja slownikow
(define dict (make-hash))
(hash-set! dict "a" ".-")
(hash-set! dict "b" "-...")
(hash-set! dict "c" "-.-.")
(hash-set! dict "d" "-..")
(hash-set! dict "e" ".")
(hash-set! dict "f" "..-.")
(hash-set! dict "g" "--.")
(hash-set! dict "h" "....")
(hash-set! dict "i" "..")
(hash-set! dict "j" ".---")
(hash-set! dict "k" "-.-")
(hash-set! dict "l" ".-..")
(hash-set! dict "m" "--")
(hash-set! dict "n" "-.")
(hash-set! dict "o" "---")
(hash-set! dict "p" ".--.")
(hash-set! dict "q" "--.-")
(hash-set! dict "r" ".-.")
(hash-set! dict "s" "...")
(hash-set! dict "t" "-")
(hash-set! dict "u" "..-")
(hash-set! dict "v" "...-")
(hash-set! dict "w" ".--")
(hash-set! dict "x" "-..-")
(hash-set! dict "y" "-.--")
(hash-set! dict "z" "--..")
(hash-set! dict "0" "-----")
(hash-set! dict "1" ".----")
(hash-set! dict "2" "..---")
(hash-set! dict "3" "...--")
(hash-set! dict "4" "....-")
(hash-set! dict "5" ".....")
(hash-set! dict "6" "-....")
(hash-set! dict "7" "--...")
(hash-set! dict "8" "---..")
(hash-set! dict "9" "----.")

(define (hash-invert hash)
  (let ([inverted (make-hash)])
    (hash-for-each hash
                   (lambda (key value)
                     (hash-set! inverted value key)))
    inverted))

(define dict-reversed (hash-invert dict))
(hash-set! dict-reversed " " " ")
;---------------------------------------------------------------------------------decode

(define (napis-skroconywl tablica)
  (if (string=? (string (car tablica)) " ")
      " "
      (napis-skrocony tablica "")))

(define (napis-skrocony tablica wynik)
      (if (null? (cdr tablica))
          (if (string=? (string (car tablica)) " ")
              wynik
              (string-append wynik (string (car tablica))))
          (if (string=? (string (car tablica)) " ")
              wynik
              (napis-skrocony (cdr tablica) (string-append wynik (string (car tablica)))))))
      

(define (reszta tablica)
  (if (null? (cdr tablica))
      ""
      (if (string=? (string (car tablica)) " ")
          (list->string (cdr tablica))
          (reszta (cdr tablica)))))


(define (morse-decode napis)
  (define pom (string->list napis))
  (define (it pom wynik)
    (if (string=? (reszta pom) "")
        (string-append wynik (hash-ref dict-reversed (napis-skroconywl pom)))
        (it
            (string->list (reszta pom))
            (string-append wynik (hash-ref dict-reversed (napis-skroconywl pom))))))
  (it pom ""))


;----------------------------------------------------------------------------------------------------------code
(define (morse-code napis)
  (define pom (string->list napis))
  (define (it tablica wynik)
    (if (null? (cdr tablica))
        (if (char-whitespace? (car tablica))
            (string-append wynik "  ")
            (string-append wynik " " (hash-ref dict (string-downcase (string (car tablica))))))
        (if (char-whitespace? (car tablica))
        (it (cdr tablica) (string-append wynik "  "))
        (it (cdr tablica) (string-append wynik " " (hash-ref dict (string-downcase (string (car tablica)))))))))
  (it pom ""))
;--------------------------------------------------------------------------------------------------------------


(morse-code "postanowienia noworoczne")
(morse-decode  ".--. --- ... - .- -. --- .-- .. . -. .. .-   -. --- .-- --- .-. --- -.-. --.. -. .")
  