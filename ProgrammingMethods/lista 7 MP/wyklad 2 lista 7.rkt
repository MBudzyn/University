#lang racket



(struct contract [wrap])
(struct jeden [jednostka jedn])
(define jt (jeden (lambda (x) x) 34))
((jeden-jednostka  jt) 4)

(define (wrap-contract c v)
  (if (contract? c)
      ((contract-wrap c) v)
  (if (c v)
      v
      (error "Contract violation"))))

(define any/c ( contract (lambda (v) v)))

(define (boolean/c v)
  (if (boolean? v)
      v
      (error "Contract violation")))

(define v (wrap-contract any/c 42))

 (define (->/c c1 c2)
  (define (wrap f)
     (lambda(x)
     (wrap-contract c2 (f (wrap-contract c1 x)))))
   (contract wrap))


(define id
  (wrap-contract (->/c boolean/c boolean/c)
     (lambda (x) x)))
  
(define (list11 . xs) xs)
(list11 1 2 3 4 5)

