#lang plait

(define (f3 f)
  (f (lambda (x) x)))

(define (zad2 x y z)
  (x z (y z)))

(define (zad1 x y)
  x)
(define (f4 f g)
  (lambda (x) (pair (f x) (g x))))

(define (f5 [f : ('a -> ( Optionof ('a * 'b )))])
  (lambda (x) (list (snd ( some-v (f x))))))

