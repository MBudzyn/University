#lang racket
(require rackunit)
(define spacja "----------------------------------------------------------------")

(provide (struct-out column-info)
         (struct-out table)
         (struct-out and-f)
         (struct-out or-f)
         (struct-out not-f)
         (struct-out eq-f)
         (struct-out eq2-f)
         (struct-out lt-f)
         table-insert
         table-project
         table-sort
         table-select
         table-rename
         table-cross-join
         table-natural-join)

(define-struct column-info (name type) #:transparent)

(define-struct table (schema rows) #:transparent)

(define cities
  (table
   (list (column-info 'city    'string)
         (column-info 'country1 'string)
         (column-info 'area    'number)
         (column-info 'capital 'boolean))
   (list (list "Wrocław" "Poland"  293 #f)
         (list "Warsaw"  "Poland"  517 #t)
         (list "Poznań"  "Poland"  262 #f)
         (list "Berlin"  "Germany" 892 #t)
         (list "Munich"  "Germany" 310 #f)
         (list "Paris"   "France"  105 #t)
         (list "Rennes"  "France"   50 #f))))


    
(define countries
  (table
   (list (column-info 'country 'string)
         (column-info 'population 'number))
   (list (list "Poland" 38)
         (list "Germany" 83)
         (list "France" 67)
         (list "Spain" 47))))

(define countries2
  (table
   (list (column-info 'country 'string)
         (column-info 'population 'number))
   (list (list "Poland" 38)
         (list "Germany" 83)
         (list "France" 67)
         (list "Spain" 47)
         (list "ukraina" 45))))

(define (empty-table columns) (table columns '()))
(define example-row (list "ukraina" 45))
; Wstawianie


(define (table-insert row tab)
   (define nowe-wiersze (append (table-rows tab) (list row)))
   (make-table (table-schema tab) nowe-wiersze))

(define k (table-insert example-row countries))
(table-rows k)
(equal? k countries2)

; Zmiana nazwy-------------------------------------------------------------------------------------------------------------


  (define (zamiananazwy col ncol schemat wynik czyzamiana)
    (cond 
      [(null? schemat) wynik]
      [(null?(cdr schemat))
       (if czyzamiana
       (append wynik (list (car schemat)))
       (append wynik (list (make-column-info ncol (column-info-type (car schemat))))))]
      [(equal?(column-info-name (car schemat)) col)
       (zamiananazwy
        col
        ncol
       (cdr schemat)
       (append wynik (list (make-column-info ncol (column-info-type (car schemat)))))
       #t)]
      [else (zamiananazwy col ncol (cdr schemat) (append wynik (list (car schemat))) czyzamiana)]))

(define (table-rename col ncol tab)
  (make-table (zamiananazwy col ncol (table-schema tab) '() #f) (table-rows tab)))

(define o (table-rename 'kraina 'capitol cities))
(pretty-print o)
spacja
        
;-----------------------------------------------------------------------------------------------------------------
  

;-------------------------------------- Projekcja

(define (lewa dane schemat wynik)
  (cond
   [(null? (cdr schemat)) (if (member (column-info-name (car schemat)) dane) (append wynik (list (car schemat))) wynik)]
   [(member (column-info-name (car schemat)) dane) (lewa dane (cdr schemat) (append wynik (list(car schemat))))]
   [else (lewa dane (cdr schemat) wynik )]))

(define (indeksy dane schemat wynik iterator)
  (cond
   [(null? (cdr schemat)) (if (member (column-info-name (car schemat)) dane) (append wynik (list iterator)) wynik)]
   [(member (column-info-name (car schemat)) dane) (indeksy dane (cdr schemat) (append wynik (list iterator)) (+ iterator 1))]
   [else (indeksy dane (cdr schemat) wynik (+ iterator 1))]))

(define c (indeksy (list 'city 'area 'capital) (table-schema cities) '() 0))

(define (skrocony-wiersz wiersz tabindeksy wynik aktualny)
  (cond
    [(null? (cdr wiersz)) (if (member aktualny tabindeksy) (append wynik (list (car wiersz))) wynik)]
    [(member aktualny tabindeksy) (skrocony-wiersz (cdr wiersz) tabindeksy (append wynik (list (car wiersz))) (+ aktualny 1))]
    [else (skrocony-wiersz (cdr wiersz) tabindeksy wynik (+ aktualny 1))]))

(define (prawy rows wynik tabindeksy)
  (cond
    [(null? (cdr rows)) (append wynik (list (skrocony-wiersz (car rows) tabindeksy '() 0)))]
    [else (prawy (cdr rows) (append wynik (list (skrocony-wiersz (car rows) tabindeksy '() 0))) tabindeksy)]))

    
(define (table-project cols tab)
  (define indekstab (indeksy cols (table-schema tab) '() 0))
  (make-table (lewa cols (table-schema tab) '()) (prawy (table-rows tab) '() indekstab)))

(define p (table-project (list 'city 'capital 'area) cities))
 (pretty-print p)
spacja
;------------------------------------------------------- Sortowanie

(define (table-sort cols tab)
 (lambda (x) x)
  )

; Selekcja

(define-struct and-f (l r))
(define-struct or-f (l r))
(define-struct not-f (e))
(define-struct eq-f (name val))
(define-struct eq2-f (name name2))
(define-struct lt-f (name val))

(define (table-select form tab)
  (lambda (x) x)
  )


; Złączenie kartezjańskie----------------------------------------------------------------------------------------
(define (polaczenie1 shema1 shema2)
(cond
  [(null? (cdr shema2)) (append  shema1 (list (car shema2)))]
  [else (polaczenie1 (append shema1 (list (car shema2))) (cdr shema2))]))

(define (polaczenie2 rows1 rows2 wynik)
  (if (null? (cdr rows2))
      (append wynik (list (append (car rows1) (car rows2))))
      (polaczenie2 rows1 (cdr rows2) (append wynik (list (append (car rows1) (car rows2)))))))

(define (polaczenie2ostateczne rows1 rows2 wynik)
  (if (null? (cdr rows1))
       (append wynik (polaczenie2 rows1 rows2 '()))
      (polaczenie2ostateczne (cdr rows1) rows2  (append wynik (polaczenie2 rows1 rows2 '())))))

(define (table-cross-join tab1 tab2)
 (make-table (polaczenie1 (table-schema tab1) (table-schema tab2))
              (polaczenie2ostateczne (table-rows tab1) (table-rows tab2)
             '())))
  
(define y (table-cross-join countries cities))

(pretty-print y)
spacja
;------------------------------------------------------------------------------------------
; Złączenie
(define (table-natural-join tab1 tab2)
  (lambda (x) x)
  )
