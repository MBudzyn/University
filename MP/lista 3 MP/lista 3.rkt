#lang racket
(require rackunit)


( define ( foldr-reverse xs )
( foldr ( lambda ( y ys ) ( append ys ( list y ) ) ) null xs ) )

( length ( foldr-reverse ( build-list 10000 identity ) ) )

;-------------------------------------------2
(define (product lista)
  (foldl * 1 lista)) ; pierwsza wartosc to dwuargumentowa funkcja druga wartosc poczatkowa trzecia lista
(product (list 1 2 3 4 5))
(product null)
;-------------------------------------------7
; w  notatniku
;-------------------------------------------3
; w  notatniku
;-------------------------------------------4
(define (zlozenie f g)
  (lambda (x)
    (f (g x))))

(define (kwadrat x)
  (* x x))
(define (dodaj1 x) (+ x 1))
(dodaj1 5)

((zlozenie dodaj1 kwadrat) 5) ;------ 26 napisana funkcja zlozenie przyjmuje jako argument dwie funkcje i zwraca funkcje lambda ktora przyjmuje jako argument x 
((zlozenie kwadrat dodaj1) 5) ;------ 36 i zwraca funkcje przyjmujaco jako argument wartosc drugiej funkcji od argumentu x
;-----------------------------------------5
(define (negatywne n)
  (build-list n
    (lambda (x)
      (+ (* x -1) -1))))

(define (odwrotnosc n)
  (build-list n
     (lambda (x)
       (/ 1 (+ x 1)))))

(define (parzyste n)
  (build-list n
     (lambda (x)
       (* x 2))))

(define (macierz n)
  (build-list n
     (lambda (x)
       (build-list n
         (lambda (y) (if (= x y) 1 0))))))
;------------------------------------------6
;reprezentacja zbioru jako funkcji jedno argumentowej ktora zwraca t jesli element nalezy do zbioru f jesli nie nalezy 
(define empty-set (lambda (x) #f))


(define (singleton a)
  (lambda (x)
    (equal? a x)))

(define (in a s) (s a)) ; wywolanie funkcji z argumentem tego elementu


(define (union s t)
  (lambda (x)
    (or (s x) (t x))))

(define (intersect s t)
  (lambda (x)
    (and (s x) (t x))))


((union (singleton 3) (singleton 4)) 4)
((intersect (singleton 3) (singleton 4)) 4)
((singleton 4) 4)
(empty-set 6)
(in 5 (singleton 3))




