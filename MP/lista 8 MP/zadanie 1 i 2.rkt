#lang racket

(define (mreverse! lst)
  (define (pom aktualny poprzedni)
    (if (null? aktualny)
        poprzedni
        (let ([next (mcdr aktualny)])
          (set-mcdr! aktualny poprzedni)
          (pom next aktualny))))
  (pom lst '()))

(define example-mlist (mcons 1 (mcons 2 (mcons 3 '()))))
(mreverse! example-mlist)
(define example-mlist2 (mcons 1 (mcons 2 (mcons 3 '()))))

(define (cycle! lst)
  (define pom lst)
  (define (it lst)
    (if (null? (mcdr lst))
        (set-mcdr! lst pom)
        (it (mcdr lst))))
  (it lst))
(cycle! example-mlist2)
example-mlist2