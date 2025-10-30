#lang racket


(define x 24)
x
(set! x (+ x 1))
x
(define (x1) 45)
x1
(x1)

(define (make-counter)
  (define cnt 0)
  (lambda ()
    (set! cnt ( + cnt 1))
    cnt))

(define m (make-counter))
(m)
(m)
(m)
