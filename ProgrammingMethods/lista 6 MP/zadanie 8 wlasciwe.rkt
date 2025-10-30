#lang plait

(define (sorted? xs)
  (cond
    [(empty? xs) #t]
    [(empty? (rest xs)) #t]
    [else (and (<= (first xs) (second xs))
               (sorted? (rest xs)))]))
               
(define (insert x xs)
  (cond
    [(empty? xs) (list x)]
    [(<= x (first xs)) (cons x xs)]
    [else (cons (first xs) (insert x (rest xs)))]))

(sorted? (list 5 4 5))
