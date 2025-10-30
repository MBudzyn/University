#lang racket

(define (+two x)
  (+ x 2))

(define (zero) 0)

(define (returns-zero)
  zero)

(define (foo)
  (define (bar x)
    (* 2 x))
  bar)

(define (baz) baz)

(define (infinite) (infinite))

(define (addition x y)
  (+ x y))

(define (return-first x y) x)

; (+ 2 (* 2 2)) -> (+ 2 4) -> 6

; gorliwa kolejność
; (addition 2 (* 2 2))
; -> (addition 2 4)
; -> (+ 2 4)
; -> 6

; (return-first (+ 1 0) (/ 1 0))
; -> (return-first 1 **wyjątek**)
; -> **wyjątek**

; leniwa kolejność
; (addition 2 (* 2 2))
; -> (+ 2 (* 2 2))
; -> (+ 2 4)
; -> 6

; (return-first (+ 1 0) (/ 1 0))
; -> (+ 1 0)
; -> 1