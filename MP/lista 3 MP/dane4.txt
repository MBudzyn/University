#lang racket

; wyprowadzenie foldr

(define (my-append xs ys)
  (if (null? xs)
      ys
      (cons (car xs) (my-append (cdr xs) ys))))

(define (my-map f xs)
  (if (null? xs)
      null
      (cons (f (car xs))
            (my-map f (cdr xs)))))

(define (my-filter p? xs)
  (if (null? xs)
      null
      (if (p? (car xs))
          (cons (car xs) (my-filter p? (cdr xs)))
          (my-filter p? (cdr xs)))))

(define (my-foldr f x xs)
  (if (null? xs)
      x
      (f (car xs) (my-foldr f x (cdr xs)))))

(define (new-append xs ys)
  (my-foldr cons ys xs))

(define (new-map f xs)
  (define (g y ys)
    (cons (f y) ys))
  (my-foldr g null xs))

(define (new-filter p? xs)
  (define (g y ys)
    (if (p? y) (cons y ys) ys))
  (my-foldr g null xs))

(define (new-map2 f xs)
  (my-foldr (lambda (y ys) (cons (f y) ys))
            null xs))

(define (new-filter2 p? xs)
  (my-foldr (lambda (y ys)
              (if (p? y) (cons y ys) ys))
            null xs))

; wyprowadzenie foldl

(define (my-length xs)
  (define (it xs acc)
    (if (null? xs)
        acc
        (it (cdr xs) (+ 1 acc))))
  (it xs 0))

(define (my-reverse xs)
  (define (it xs acc)
    (if (null? xs)
        acc
        (it (cdr xs) (cons (car xs) acc))))
  (it xs null))

(define (my-sum xs)
  (define (it xs acc)
    (if (null? xs)
        acc
        (it (cdr xs) (+ (car xs) acc))))
  (it xs 0))

(define (my-foldl f x xs)
  (define (it xs acc)
    (if (null? xs)
        acc
        (it (cdr xs) (f (car xs) acc))))
  (it xs x))

(define (my-sum2 xs)
  (my-foldl + 0 xs))

(define (my-reverse2 xs)
  (my-foldl cons null xs))

(define (my-length2 xs)
  (my-foldl (lambda (y acc) (+ 1 acc)) 0 xs))

(define (weird-map2 f xs)
  (my-foldl (lambda (y ys) (cons (f y) ys))
            null xs))

(define (weird-append xs ys)
  (my-foldl cons ys xs))

; działanie foldl i foldr

; (my-foldr f x (list 1 2 3 4))
; (my-foldr f x (cons 1 (cons 2 (cons 3 (cons 4 null)))))
; (f 1 (f 2 (f 3 (f 4 x))))
; infiksowo, przyjmijmy f = +
; (1 + (2 + (3 + (4 + x))))

; (my-fold1 f x (list 1 2 3 4))
; (my-foldl f x (cons 1 (cons 2 (cons 3 (cons 4 null)))))
; (it (cons 1 (cons 2 (cons 3 (cons 4 null)))) x)
; (it (cons 2 (cons 3 (cons 4 null))) (f 1 x)))
; (it (cons 3 (cons 4 null)) (f 2 (f 1 x)))
; (it null (f 4 (f 3 (f 2 (f 1 x)))))
; (f 4 (f 3 (f 2 (f 1 x))))

; załóżmy, że f przyjmuje argumenty w odwrotnej kolejności
; (f (f (f (f x 1) 2) 3) 4)
; infiksowo, przyjmijmy f = +
; ((((x + 1) + 2) + 3) + 4)

; zapis infiksowy 1 + 2
; zapis prefiksowy + 1 2
; zapis postfiksowy 1 2 +