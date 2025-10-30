#lang plait



(define (foo lista)
  (foldl
   (lambda (x  y) (* x y))
   1
   lista))
(foo (list 1 2 3 4 9))

#;
(define (sumalit lista)
  (local
    (define (it lista wynik)
      (if (null? lista)
          wynik
          (it (rest lista) (+ wynik (first lista)))))
  (it lista 0)))

(define (sumalit lista)
  (local
    [(define (it lista wynik)
      (if (empty? lista)
          wynik
          (it (rest lista) (+ wynik (first lista)))))]
  (it lista 0)))

(define (sum xs)
  (local [(define (it xs acc)
            (if (empty? xs)
                acc
                (it (rest xs) (+ acc (first xs)))))]
    (it xs 0)))

(empty? '())
