#lang plait

(define-syntax my-and
  (syntax-rules ()
    ((_ x) x)
    ((_ x y ...)
     (if x (my-and y ...) #f))))

(define-syntax my-or2
  (syntax-rules ()
    ((_ x) x)
    ((_ x y ...)
       (if x x (my-or2 y ...)))))

(define-syntax my-let
  (syntax-rules ()
    ((_ ((var expr) ...) body)
     ((lambda (var ...) body) expr ...))))

(define-syntax my-let*
  (syntax-rules ()
    ((_ () body)
     body)
    ((_ ((var expr) . rest) body)
     (my-let ((var expr))
       (my-let* rest body)))))



(my-and #t #t #f)
(my-or2 #f #f #t)    
(my-let ((x 5)
          (y 10))
  (+ x y))        

(my-let* ((x 5)
           (y (+ x 10)))
  (+ x y))         