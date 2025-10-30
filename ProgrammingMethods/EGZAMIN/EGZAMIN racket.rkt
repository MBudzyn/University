#lang racket
(require rackunit)

;----------------------
(let ([x 5])
    (let ([x 2]
          [y x]) ; do przypisujemy wartosc 5 poniewaz x o wartosci 2 nie jest widoczny w tym lecie
      (list y x))) ; ale w wyrazeniu juz  jest co w wyniku da 5 2
;----------------------
(cons 1 2)
'(1 . 2)

(cons 1 '())
'(1)

(cons 1 (list 2 3 4))
'(1 2 3 4)

(cons (list 1 2 3) (list 4 5 6))
'((1 2 3) 4 5 6)

(cons (list 1 2 3) 4)
'((1 2 3) . 4)
;-----------------------------------
(foldl cons '() '(1 2 3 4))
'(4 3 2 1)

(foldl + 0 '(1 2 3 4)) ; 1+0 -> 2 + 1 -> 3 + 3 -> 4 + 6 najpierw element listy potem "pojemnik"(wynik)
10

(foldl (lambda (x y) (- y x)) 0 '(1 2 3 4))
-10

(define (insert element lista)
  (cond
     [(equal? lista null) (cons element null)]
     [(< element (car lista)) (cons element lista)]
     [else (cons (car lista) (insert element (cdr lista)))]))

(define (insert-sort lista1 lista2)
  (cond
    [(equal? lista2 null) lista1]
    [(insert-sort (insert (car lista2) lista1) (cdr lista2))]))

(insert-sort (list 1 3 5 5 7 9) (list 1 4 2 1 4  5 2 1))


(define (mniejsze_5 lista)
  (filter (lambda (x) (if (< x 5) #t #f)) lista))

(define ( kwadrat liczba)
  (* liczba liczba))

(define (kwadraty lista)
  (map kwadrat lista))

(define (suma_mniejszych_5 lista)
  (foldr (lambda (x y) (if (< x 5) (+ x y) y)) 0 lista))

(suma_mniejszych_5 (list 1 2 3 9 5 4 0 3 4 2 9))

(define-struct leaf () #:transparent)
(define-struct node (l e r) #:transparent)


(define (find_el tree x)
  (cond
    [(leaf? tree) #f]
    [(node? tree)
     (cond
       [(= x (node-e tree)) #t]
       [(< x (node-e tree)) (find_el (node-l tree) x)]
       [else (find_el (node-r tree) x)])]))


(define example-tree (node (node (leaf) 1 (leaf))
                           2
                           (node (node (leaf) 3 (leaf))
                                 4
                                 (node (leaf) 5 (leaf)))))

(find_el example-tree 6)
     
 #|           
(define/contract (funkcja list1 list2)
  (parametric->/c [a b c] (-> (listof a) (listof b) (listof c)))
  (let ((suma (foldl + 0 list1)))
    (map (lambda (x) (+ suma x)) list2)))
|#

(define/contract (map f xs)
  (parametric->/c [a b] (-> (-> a b) (listof a) (listof b)))
  (match xs
    ['() null]
    [(cons x xs) (cons (f x) (map f xs))]))
    


(map kwadrat (list 2 3 4))

(define (my-foldl function acc list)
  (if (null? list)
      acc
      (my-foldl function (function acc (car list)) (cdr list))))

(my-foldl + 0 '())

(define (split lst)
  (define len (length lst))
  (define mid (quotient len 2))
  (if (odd? len)
      (cons (take lst (add1 mid)) (drop lst (add1 mid)))
      (cons (take lst mid) (drop lst mid))))

(car (split (list 1 2 3 4 5 3 2 0)))

(cdr (split (list 1 2 3 4 5 3 2 0)))

(define (return_sum lista)
  (filter (lambda (x) (> x 3)) lista))
(return_sum (list 1 2 3 4 5 6 2 1 4 0 9))

(cons '() 5)
(cons (list 3) (list 3 4))
(build-list 9 (lambda (x) (- 0 x)))

(for-each (lambda (x) (display (+ x 3))) (list 1 2 3 4))
(define/contract (apply f arg)
(parametric->/c [a b] (-> (-> a b) a b))
(f arg))

(define/contract (do f1 listaarg)
(parametric->/c [a] (-> (-> a boolean?) (listof a) ( cons/c ( listof a) ( listof a))))
(if (f1 (car listaarg))
    (cons listaarg listaarg)
    (cons listaarg listaarg)))


(define (wieksze5 x)
  (if (> x 5) #t #f))


(define (kwadrato a)
  (* a a))
(define spacja "---------------------------------------------")
spacja
(apply kwadrat 5)


(define/contract
  (do2 listaf listaarg)
  (parametric->/c [a b]
    (-> (listof (-> a b))
        (listof a)
        (listof b)))
  (define (it wynik listaf listaarg)
    (if (or (null? listaf) (null? listaarg))
        wynik
        (it (cons ((car listaf) (car listaarg)) wynik)
            (cdr listaf)
            (cdr listaarg))))
  (it '() listaf listaarg))

(do2 (list (lambda (x) (* x x)) (lambda (x) (* x x))) (list 3 4 5 6))
(do wieksze5 (list 1 2 3 4))


(define/contract (fo f as)
    (parametric->/c [a] (-> (-> a boolean?) ( listof a) ( cons/c ( listof a) ( listof a))))
    (define (it f as wynik)
      (cond
        [(null? as) wynik]
        [(f (car as))
         (it f (cdr as) (cons (cons (car as) (car wynik)) (cdr wynik)))]
        [else (it f (cdr as) (cons (car wynik) (cons (car as) (cdr wynik))))]))
  (it f as (cons '() '())))

(fo wieksze5 (list 1 2 9 3 0 4 3 0 3 0 4   7 9 5 9 4 9))

(define/contract (fo2 f b)
    (parametric->/c [a b] (-> (-> b (or/c false/c ( cons/c a b))) b ( listof a)))
  (define (it f b wynik)
    (cond
      [(eq? (f b) #f) wynik]
      [else (it f (cdr (f b)) (cons (car (f b)) wynik))]))
  (it f b '()))




(define (cos arg)
  (if (< arg 5) #f (cons 5 (- arg 1))))
 
(fo2 cos 10)

(define (dodaj3 x y z)
  (+ x (+ y z)))
(map kwadrat  (list 1 4 3 5))


(foldr (lambda (x y) (cons (cons x #t) y)) '() (list 1 2 3 4))

(filter (lambda (x) (< x 5)) (list 1 2 3 8 5 0 3 9 2 9 3  9 ))

(define (make-a liczba)
  (define (it liczba wynik)
    (if (= liczba 0)
        wynik
        (it (- liczba 1) (cons "a" wynik))))
  (it liczba '()))

(build-list 10 make-a)
(modulo 133 34)
(length (list 1 2 3 21134 14 12231 'sdga 'w4t))

(reverse (list 3 4 5 6))

(define p (cons 1 "koniczyna"))
p

(empty? '())
(define-struct czlowiek (wiek plec zainteresowanie) #:mutable)
(define jarek (czlowiek 18 "m" "gała"))
(czlowiek-wiek jarek)
(set-czlowiek-wiek! jarek 20)
(czlowiek-wiek jarek)

(eq? (empty? '()) (null? '()))
(struct polska (ilosc jakos niewiem) #:mutable)
(define p1 (polska 3 4 5))
(polska-ilosc p1)
(set-polska-ilosc! p1 10)
(polska-ilosc p1)
(define (mniejszy a b)
  (if (< a b) a b))


(define (min lista)
  (define (it lista wynik)
    (cond
      [(empty? lista) wynik]
      [(< (car lista) wynik) (it (cdr lista) (car lista))]
      [else (it (cdr lista) wynik)]))
  (it lista +inf.0))


(define (bezel lista el)
  (cond
    [(empty? lista) '()]
    [(eq? (car lista) el) (cdr lista)]
    [else (cons (car lista) (bezel (cdr lista) el))]))

(define (selectsort lista)
  (if (empty? lista) '()
 (let* ([mini (min lista)]
                [reszta (bezel lista mini)])
           (cons mini (selectsort reszta)))))

(selectsort (list))
         



  

  