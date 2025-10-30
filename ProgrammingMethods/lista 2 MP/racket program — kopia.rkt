#lang racket
(require rackunit)

;-----------------------------------------------------2
(define (fibo n)
  (cond [(= n 0) 0]
        [(= n 1) 1]
        [else ( + (fibo (- n 1)) (fibo (- n 2)))]))


(define (fibo-iter n)
  (define (it n k  z1 z2 w)
    (if (= k n)
        w
        (it n (+ k 1) z2 (+ z1 z2) (+ z1 z2))))
  (it n 0 1 0 0))

(fibo-iter 4)
(fibo-iter 5)
(fibo-iter 6)
(fibo-iter 7)
(fibo-iter 8)
(define a "-----------")
a
(fibo 4)
(fibo 5)
(fibo 6)
(fibo 7)




;----------------------------------------------------5
(define (elem? x lista)
  (cond [(null? lista) #f]
        [(= (first lista) x) #t]
        [else (elem? x (cdr lista))]))

(elem? 6 (list 7 2 5 4 3))
;----------------------------------------------------6
(define (wieksza a b)
  (if (> a b) a b))

(define (max lista w)
  (if (null? lista)
     w (max (cdr lista) (wieksza w (first lista)))))


(max (list 1 2 5 0 9 3 2 23 12435 0 3) -inf.0)


;-------------------------------------------------8

(define (sorted lista)
  (cond [ (null? lista) #t]
        [ (null? (cdr lista)) #t]
        [ (> (car lista) ( car (cdr lista))) #f]
        [else (sorted (cdr lista))]))

(sorted (list 1 2 3 4 5 5 ))
;----------------------------------------------3

(define-struct macierz (a b c d))

(define f (make-macierz 1 3 7 0))


(define (mnozenie m1 m2)
  (define w (+ (* (macierz-a m1) (macierz-a m2)) (* (macierz-b m1) (macierz-c m2))))
  (define x (+ (* (macierz-a m1) (macierz-b m2)) (* (macierz-b m1) (macierz-d m2))))
  (define y (+ (* (macierz-c m1) (macierz-a m2)) (* (macierz-d m1) (macierz-c m2))))
  (define z (+ (* (macierz-c m1) (macierz-b m2)) (* (macierz-d m1) (macierz-d m2))))
  (make-macierz w x y z))

(define matrix-id (make-macierz 1 0 0 1))

(define fibomacierz (make-macierz 1 1 1 0))

(define (potegaminter m1 k)
  (define (iter wynik m1 k)
    (cond [(= k 0) matrix-id]
        [(= k 1) wynik]
        [else (iter (mnozenie wynik m1) m1 (- k 1))]))
  (iter m1 m1 k))

  (define (fibom k)
  (define (iter wynik m1 k)
    (cond [(= k 0) matrix-id]
        [(= k 1) wynik]
        [else (iter (mnozenie wynik m1) m1 (- k 1))]))
  (iter fibomacierz fibomacierz (- k 1)))


a
(macierz-a (fibom 2))
(macierz-a (fibom 3))
(macierz-a (fibom 4))
(macierz-a (fibom 5))
(macierz-a (fibom 6))
a
(macierz-a (potegaminter f 3))
a
(macierz-a (mnozenie f f))
a
;-----------------------------------------------------------------9
(define (mniejsza a b)
  (if (< a b) a b))

(define (minimum lista w)
  (if (null? lista)
     w
     (minimum (cdr lista) (mniejsza w (first lista)))))

(define (select lista)
  (let ([najmniejszy (minimum lista +inf.0)]) (cons najmniejszy (remove najmniejszy lista))))

(define (select-sort lista)
  (let ([zmienna (select lista)])
    (if (null? (cdr zmienna))
        zmienna
        (cons (car zmienna) (select-sort (cdr zmienna))))))
      
  
(select-sort (list 25 32241 123 1234 54 1 2151235 123))
;-------------------------------------------------------7
(define (sufix lista)
  (if (null? lista)
      (list null)
      (cons lista (sufix (cdr lista)))))
a
(sufix (list 1 3 5 2 3 4 5))

;------------------------------------------------------------