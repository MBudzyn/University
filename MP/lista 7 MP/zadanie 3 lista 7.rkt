#lang racket

(define/contract (suffixes lst)
  (-> (listof any/c) (listof (listof any/c)))
  (define (it lst result)
    (if (null? lst)
        result
        (it (cdr lst) (cons lst result))))

  (it lst '()))

(define (suffixes2 lst)
  (define (it lst result)
    (if (null? lst)
        result
        (it (cdr lst) (cons lst result))))

  (it lst '()))

;; test
(define lst (range 3000))
(time (suffixes lst)) ;bardzo oodobne czasy dzialania
(time (suffixes2 lst))  ;bardzo oodobne czasy dzialania
(suffixes (list 1 2 3 4 5))