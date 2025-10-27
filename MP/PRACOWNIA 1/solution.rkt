#lang racket
(require rackunit)
(require racket/list)
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
         (column-info 'country 'string)
         (column-info 'area    'number)
         (column-info 'capital 'boolean))
   (list (list "Wrocław" "Poland"  293 #f)
         (list "Warsaw"  "Poland"  517 #t)
         (list "Poznań"  "Poland"  262 #f)
         (list "Berlin"  "Germany" 892 #t)
         (list "Munich"  "Germany" 310 #f)
         (list "Paris"   "France"  105 #t)
         (list "Rennes"  "France"   50 #f))))


(define cities3
  (table
   (list (column-info 'city    'string)
         (column-info 'country 'string)
         (column-info 'area    'number)
         (column-info 'capital 'boolean))
   (list (list "Wrocław" "Poland"  293 #f)
         (list "Poland"  "Poland"  517 #t)
         (list "Poznań"  "Poland"  262 #f)
         (list "Berlin"  "Germany" 892 #t)
         (list "Munich"  "Germany" 310 #f)
         (list "Paris"   "France"  105 #t)
         (list "Rennes"  "France"   50 #f)
         (list "urocław" "Poland"  600 #f)
         (list "larsaw"  "Poland"  123 #f)
         (list "Poznań"  "Poland"  261 #f)
         (list "Berlin"  "Germany" 892 #f)
         (list "Munich"  "Germany" 311 #f)
         (list "Paris"   "France"  105 #f)
         (list "Rennes"  "France"  1200 #f)
         (list "Poland" "Poland"  293 #f)
         (list "Warsaw"  "Poland"  100 #t)
         (list "Poznań"  "Poland"  262 #f)
         (list "Berlin"  "Germany" 892 #t)
         (list "Germany"  "Germany" 310 #f)
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
(define example-row1 (list "ukraina" 45 23))
(define example-row2 (list "ukraina" '90))
(define example-row3 (list 4443 45))
(define example-row4 '())

; Wstawianie-------------------------------------------------------------------------------------------------------------

(define (tabtypow shema wynik)
  (if
    (null? (cdr shema))
       (append
           wynik
           (list (column-info-type (car shema))))
       (tabtypow
           (cdr shema)
           (append
                wynik
                (list (column-info-type (car shema)))))))


(define (my-length xs)
  (define (it xs acc)
    (if (null? xs)
        acc
        (it (cdr xs) (+ 1 acc))))
  (it xs 0))
      
    
(define i (tabtypow (table-schema cities) '()))
(define (czyzgodne tablicatypow dane)
  (cond
    [(and (null? tablicatypow) (null? dane)) #t]
    [(not (= (my-length tablicatypow) (my-length dane)) ) #f]
    [(null? (cdr dane))
            (cond
      [(equal? 'number (car tablicatypow))
          (if (number? (car dane))
              #t
              #f)]
      [(equal? 'string (car tablicatypow))
          (if (string? (car dane))
              #t
              #f)]
      [(equal? 'symbol (car tablicatypow))
          (if (symbol? (car dane))
              #t
              #f)]
      [(equal? 'boolean (car tablicatypow))
          (if (boolean? (car dane))
              #t
              #f)]
      [else #f])]
    
      [(equal? 'number (car tablicatypow))
          (if (number? (car dane))
              (czyzgodne (cdr tablicatypow) (cdr dane))
              #f)]
      [(equal? 'string (car tablicatypow))
          (if (string? (car dane))
              (czyzgodne (cdr tablicatypow) (cdr dane))
              #f)]
      [(equal? 'symbol (car tablicatypow))
          (if (symbol? (car dane))
              (czyzgodne (cdr tablicatypow) (cdr dane))
              #f)]
      [(equal? 'boolean (car tablicatypow))
          (if (boolean? (car dane))
              (czyzgodne (cdr tablicatypow) (cdr dane))
              #f)]
      [else #f])) 




(define (table-insert row tab)
  (define nowe-wiersze
     (append
        (table-rows tab)
        (list row)))
  (if (equal? (table-schema tab) '())
      (error "nieprawidlowy wiersz do wstawienia")
  (if (czyzgodne
       (tabtypow (table-schema tab) '())
        row) 
   (make-table (table-schema tab) nowe-wiersze)
   (error "nieprawidlowy wiersz do wstawienia"))))


;(pretty-print (table-insert example-row countries))
;(pretty-print (table-insert example-row1 countries))
;(pretty-print (table-insert example-row2 countries))
;(pretty-print (table-insert example-row3 countries))
;(pretty-print (table-insert example-row4 countries))


; Zmiana nazwy-------------------------------------------------------------------------------------------------------------


  (define (zamiananazwy col ncol schemat wynik czyzamiana)
    (cond 
      [(null? schemat) wynik]
      [(null?(cdr schemat))
         (if czyzamiana
            (append
                wynik
                (list (car schemat)))
            (append
                wynik
                (list (make-column-info ncol (column-info-type (car schemat))))))]
      [(equal?(column-info-name (car schemat)) col)
       (zamiananazwy
           col
           ncol
           (cdr schemat)
           (append
               wynik
               (list (make-column-info ncol (column-info-type (car schemat)))))
       #t)]
      [else
          (zamiananazwy
              col
              ncol
              (cdr schemat)
              (append
                   wynik
                   (list (car schemat)))
              czyzamiana)]))

(define (table-rename col ncol tab)
  (if (equal? (table-schema tab) '())
      tab
  (make-table
      (zamiananazwy
          col
          ncol
          (table-schema tab)
          '()
          #f)
      (table-rows tab))))

(define o (table-rename 'kraina 'capitol cities))
(pretty-print o)
spacja
        
;-----------------------------------------------------------------------------------------------------------------
  

;-------------------------------------- Projekcja

(define (lewa dane schemat wynik)
  (cond
   [(null? (cdr schemat))
       (if (member
               (column-info-name (car schemat))
               dane)
           (append
               wynik
               (list (car schemat)))
           wynik)]
   [(member
        (column-info-name (car schemat))
        dane)
    (lewa
        dane
        (cdr schemat)
        (append
            wynik
            (list(car schemat))))]
   [else (lewa
             dane
             (cdr schemat)
             wynik )]))

(define (indeksy dane schemat wynik iterator)
  (cond
   [(null? (cdr schemat))
       (if (member
               (column-info-name (car schemat))
               dane)
           (append
               wynik
               (list iterator))
           wynik)]
   [(member
        (column-info-name (car schemat))
        dane)
    (indeksy
        dane
        (cdr schemat)
        (append
             wynik
             (list iterator))
        (+ iterator 1))]
   
   [else (indeksy
             dane
             (cdr schemat)
             wynik
             (+ iterator 1))]))

(define c (indeksy (list 'city 'area 'capital) (table-schema cities) '() 0))

(define (skrocony-wiersz wiersz tabindeksy wynik aktualny)
  (cond
    [(null? (cdr wiersz))
     (if (member aktualny tabindeksy)
         (append wynik (list (car wiersz)))
          wynik)]
    [(member aktualny tabindeksy)
     (skrocony-wiersz
       (cdr wiersz)
        tabindeksy
       (append wynik (list (car wiersz)))
       (+ aktualny 1))]
    [else (skrocony-wiersz
          (cdr wiersz)
           tabindeksy
           wynik
          (+ aktualny 1))]))

(define (prawy rows wynik tabindeksy)
  (cond
    [(null? rows) wynik]
    [(null? (cdr rows))
     (append wynik (list (skrocony-wiersz (car rows) tabindeksy '() 0)))]
    [else (prawy
              (cdr rows)
              (append wynik (list (skrocony-wiersz (car rows) tabindeksy '() 0)))
               tabindeksy)]))

    
(define (table-project cols tab)
  (define indekstab (indeksy cols (table-schema tab) '() 0))
  (if (or (empty? cols) (empty? (table-schema tab)))
      '()
  (make-table (lewa cols (table-schema tab)'())
              (prawy (table-rows tab) '() indekstab))))

(define p (table-project (list 'city 'capital 'area) cities))
(define p1 (table-project (list  '2423 'city 'area) cities))
(define p2 (table-project (list  'country) countries))
(define p3 (table-project (list  '2423 'city 'area) countries))
(define p4 (table-project (list  '2423 'city 'area) cities3))

 (pretty-print p1)
 (pretty-print p2)
 (pretty-print p3)
 (pretty-print p4)


 (pretty-print p)
spacja
;------------------------------------------------------- Sortowanie

;(index-of lst 'b)

 (define (nazwyschema schema wynik)
   (cond
     [(null? schema) '()]
     [(null? (cdr schema)) (append wynik (list  (column-info-name (car schema))))]
     [else (nazwyschema (cdr schema) (append wynik (list (column-info-name (car schema)))))]))
             
(define (indeksy2 nazwy zbiordanych wynik)
  (cond
    [(null? nazwy) '()]
    [(null? (cdr nazwy)) (append wynik  (list (index-of zbiordanych (car nazwy))))]
    [else (indeksy2 (cdr nazwy) zbiordanych (append wynik (list (index-of zbiordanych (car nazwy)))))]))
       



(define (boolean< x y)
  (if (and (not x)  y)
      #t
      #f))

(define (boolean= x y)
  (or (and x y) (and (not x) (not y))))

(define (symbol< x y)
  (define k (symbol->string x))
  (define z (symbol->string y))
  (string<? k z))

(define (symbol= x y)
  (define k (symbol->string x))
  (define z (symbol->string y))
  (string=? k z))

(define (sort-by-indices lsts indices)
  (define (compare-indexed-lists lst1 lst2)
    (define (compare-indexed-lists2 lst1 lst2 indices)
      (cond ((null? lst1) #t)
          ((number? (list-ref lst1 (car indices)))
           (cond ((< (list-ref lst1 (car indices))
                     (list-ref lst2 (car indices))) #t)
                 ((= (list-ref lst1 (car indices))
                     (list-ref lst2 (car indices)))
                  (if (null? (cdr indices))
                      #t
               (compare-indexed-lists2 lst1 lst2 (cdr indices))))
                 (else #f)))
          
          ((boolean? (list-ref lst1 (car indices)))
           (cond ((boolean< (list-ref lst1 (car indices))
                            (list-ref lst2 (car indices))) #t)
                 ((boolean= (list-ref lst1 (car indices))
                            (list-ref lst2 (car indices)))
                  (if (null? (cdr indices))
                      #t
               (compare-indexed-lists2 lst1 lst2 (cdr indices))))
                 (else #f)))
           
          ((string? (list-ref lst1 (car indices)))
           (cond ((string<? (list-ref lst1 (car indices))
                            (list-ref lst2 (car indices))) #t)
                 ((string=? (list-ref lst1 (car indices))
                            (list-ref lst2 (car indices)))
                  (if (null? (cdr indices))
                      #t
               (compare-indexed-lists2 lst1 lst2 (cdr indices))))
                 (else #f)))
           
          ((symbol? (list-ref lst1 (car indices)))
           (cond ((symbol< (list-ref lst1 (car indices))
                            (list-ref lst2 (car indices))) #t)
                 ((symbol= (list-ref lst1 (car indices))
                            (list-ref lst2 (car indices)))
                  (if (null? (cdr indices))
                      #t
               (compare-indexed-lists2 lst1 lst2 (cdr indices))))
                 (else #f)))
          (else #f)))
    (compare-indexed-lists2 lst1 lst2 indices))
  (sort lsts compare-indexed-lists))


(define (table-sort cols tab)
  (if (null? cols)
      tab
(make-table (table-schema tab)
           (sort-by-indices (table-rows tab) (indeksy2 cols (nazwyschema (table-schema tab) '()) '())))))


(define kt1 (table-sort (list 'area 'capital 'country) cities3))
(define kt2 (table-sort (list 'capital 'area 'country) cities3))
(define kt3 (table-sort (list 'country 'area 'capital ) cities3))
(define kt4 (table-sort '() cities3))
(define kt5 (table-sort (list 'area) cities3))
(pretty-print kt1)
(pretty-print kt2)
(pretty-print kt3)
(pretty-print kt4)
(pretty-print kt5)


; ------------------------------------------------------------Selekcja

(define (mniejsze arg1 arg2)
  (cond
    [(number? arg1) (< arg1 arg2)]
    [(boolean? arg1) (boolean< arg1 arg2)]
    [(string? arg1) (string<? arg1 arg2)]
    [else (symbol< arg1 arg2)]))



(define (wspolne list1 list2)
  (filter (lambda (x) (member x list2)) list1))

(indeksy (list 'capital 'country) (table-schema cities) '() 0)

(define (tabeq-f rows indeks val wynik)
  (cond
    [(null? rows) '()]
    [(null? (cdr rows))
     (if (equal? (list-ref (car rows)  indeks) val)
         (append wynik (list (car rows)))
         wynik)]
    [(equal? (list-ref (car rows) indeks) val) (tabeq-f (cdr rows) indeks val (append wynik (list (car rows))))] 
    [else (tabeq-f (cdr rows) indeks val wynik )]))



(define (tablt-f rows indeks val wynik)
  (cond
    [(null? rows) '()]
    [(null? (cdr rows))
     (if (mniejsze (list-ref (car rows)  indeks) val)
         (append wynik  (list (car rows)))
         wynik)]
    [(mniejsze (list-ref (car rows) indeks) val) (tablt-f (cdr rows) indeks val (append wynik (list (car rows))))] 
    [else (tablt-f (cdr rows) indeks val wynik )]))




(define (tabeq-f2 rows indeks1 indeks2 wynik)
  (cond
    [(null? rows) '()]
    [(null? (cdr rows))
     (if (equal? (list-ref (car rows) indeks1) (list-ref (car rows) indeks2))
         (append wynik (list (car rows)))
         wynik)]
    [(equal? (list-ref (car rows)  indeks1) (list-ref (car rows) indeks2)) (tabeq-f2 (cdr rows) indeks1 indeks2 (append wynik (list (car rows))))]
    [else (tabeq-f2 (cdr rows) indeks1 indeks2 wynik )]))
     


  

(remove* (list 2 4) (list 1 2 3 4 5)) ; zwroci 1 3 5
(define-struct and-f (l r))
(define-struct or-f (l r))
(define-struct not-f (e))
(define-struct eq-f (name val))
(define-struct eq2-f (name name2))
(define-struct lt-f (name val))
;(define (indeksy dane schemat wynik iterator)   (define (tabeq-f rows indeks val wynik) (define (tabeq-f2 rows indeks1 indeks2 wynik)
(remove* (list 2 4) (list 1 2 3 4 5)) ; zwroci 1 3 5
(define (table-selectpom form tab)
  (cond
    [(and-f? form)
        (wspolne
            (table-selectpom (and-f-l form) tab)
            (table-selectpom (and-f-r form) tab))]
    [(or-f? form)
        (append
            (table-selectpom (or-f-l form) tab)
            (table-selectpom (or-f-r form) tab))]
    [(not-f? form)
        (remove*
            (table-selectpom (not-f-e form) tab)
            (table-rows tab))]
    [(eq-f? form)
        (tabeq-f
            (table-rows tab)
            (index-of (nazwyschema (table-schema tab) '()) (eq-f-name form))
            (eq-f-val form)
            '())]
    [(eq2-f? form)
        (tabeq-f2
           (table-rows tab)
           (index-of (nazwyschema (table-schema tab) '()) (eq2-f-name form))
           (index-of (nazwyschema (table-schema tab) '()) (eq2-f-name2 form))
           '())]
    [(lt-f? form)
        (tablt-f
           (table-rows tab)
           (index-of (nazwyschema (table-schema tab) '()) (lt-f-name form))
           (lt-f-val form)
           '())]))

(define (table-select form tab)
   (make-table
       (table-schema tab)
       (table-selectpom form tab)))
    

(define forma1 (not-f (or-f (eq-f 'capital #f)
( lt-f 'area 520))))



; Złączenie kartezjańskie----------------------------------------------------------------------------------------
(define (polaczenie1 shema1 shema2)
(cond
  [(null? (cdr shema2))
       (append  shema1 (list (car shema2)))]
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
  (cond
    [(null? tab1) tab2]
    [(null? tab2) tab1]
    [else (make-table (polaczenie1 (table-schema tab1) (table-schema tab2))
             (polaczenie2ostateczne (table-rows tab1) (table-rows tab2) '()))]))
  
(define y (table-cross-join countries cities))
(define y2 (table-cross-join countries '()))
(define y3 (table-cross-join '() cities))
(define y4 (table-cross-join cities countries))
(define y5 (table-cross-join countries cities3))
(pretty-print y)
(pretty-print y5)
(pretty-print y2)
(pretty-print y3)
(pretty-print y4)
spacja
;------------------------------------------------------------------------------------------
; Złączenie

(define (schema-names schema wynik)
  (cond [(null? (cdr schema)) (append wynik (list (column-info-name (car schema))))]
        [else (schema-names (cdr schema) (append wynik (list (column-info-name (car schema)))))]))


(define (polaczenienatsche schema1 schema2 schema1-name)
  (cond
    [(null? schema2) schema1]
    [(member (column-info-name (car schema2)) schema1-name) (polaczenienatsche schema1 (cdr schema2) schema1-name)]
    [else (polaczenienatsche (append schema1 (list (car schema2))) (cdr schema2) schema1-name)]))

(define (indeksydododania schema1 schema2 schema1-name wynik)
  (cond
    [(null? (cdr schema2))
     (if (member (column-info-name (car schema2)) schema1-name)
         wynik
         (append wynik (list (column-info-name (car schema2)))))]
    [(member (column-info-name (car schema2)) schema1-name)(indeksydododania schema1 (cdr schema2) schema1-name wynik)]
    [else (indeksydododania schema1 (cdr schema2) schema1-name (append wynik (list (column-info-name (car schema2)))))]))
  


(pretty-print (table-project (schema-names (table-schema countries) '()) countries))

(define b (polaczenienatsche (table-schema countries) (table-schema cities) (schema-names (table-schema countries)  '())))
(define bw (indeksydododania (table-schema countries) (table-schema cities) (schema-names (table-schema countries) '()) '() ))
(define (table-natural-join tab1 tab2)
  0)

;-----------------------------------------------------------------------------------------------------------------------------------



