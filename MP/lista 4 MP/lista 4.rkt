#lang racket
(require rackunit)


(define-struct leaf () #:transparent)
(define-struct node (l elem r) #:transparent)


( define o
( node
( node ( leaf ) 2 ( leaf ) )
5
( node ( node ( leaf ) 6 ( leaf ) )
8
( node ( leaf ) 9 ( leaf ) ) ) ) )


(define (tree? x)
  (cond [(leaf? x) #t]
        [(node? x) (and (tree? (node-l x))
                        (tree? (node-r x)))]
        [else #f]))

(define example-tree
  (node (node (leaf) 1 (leaf))
        2
        (node (node (leaf) 3 (leaf))
              4
              (leaf))))
;----------------------------------------------------------3
(define (suma t)
(define (sum-paths t w)
  (cond [(leaf? t) t]
        [(node? t)
         (make-node
          (sum-paths (node-l t) (+ w (node-elem t)))
          (+ (node-elem t) w)
          (sum-paths (node-r t) (+ w (node-elem t))))]))
  (sum-paths t 0))


(define (bst? tree)
  (cond [(leaf? tree) #t]
        [(leaf? (node-l tree))
         (bst? (node-r tree))]
        [(leaf? (node-r tree))
         (bst? (node-l tree))]
        [(<= (node-elem tree)
             (node-elem (node-l tree)))
         #f]
        [(>= (node-elem tree)
             (node-elem (node-r tree)))
         #f]
        [(and (bst? (node-l tree))
              (bst? (node-r tree)))]
        ))
;------------------------------------------------------------

(define (fold-tree f wynik tree)
    (cond [(leaf? tree) wynik]
          [(node? tree)
           (f
            (fold-tree f wynik (node-l tree))
            (node-elem tree)
            (fold-tree f wynik (node-r tree)))]))



(define (tree-flip t)
  (fold-tree (lambda (x y z) (node z y x)) (leaf) t))

(define (tree-height t)
  (fold-tree (lambda (l val r) (+ 1 (max l r))) 0 t))



(define (flatten t)
  (fold-tree (lambda (l val r) (append l (cons val r))) '() t))


;--------------------------------------------

;---------------------------------------------

(bst? example-tree)
;----------------------------------------------
(fold-tree + 0 o)
(fold-tree + 0 o)
;----------------------------------------------7
(define empty-queue (cons null null))

(define ( empty? q )
(and
  (null? (car q))
  (null? (cdr q))))


(define ( push-back x q) 
 (cons (car q) (cons x (cdr q))))

(define lista1 (list 1 2 3))
(define lista2 (list 4 5 6))
(define fifo (list lista1 lista2))


(define( front q) 
(car (car q)))

(define (pop q)
  (czypusta
   (cons (cdr (car q)) (cdr q))))

(define (czypusta q)
  (if (and (null? (car q)) (not (null? (cdr q))))
      (cons (reverse (cdr q)) null)
      q))
;---------------------------------------------

