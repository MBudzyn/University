#lang racket
(require rackunit)

(struct mqueue
  ([front #:mutable] [back #:mutable]))

(define (mqueue-empty? q)
  (null? (mqueue-front q)))

(define nonempty-mqueue/c
  (and/c mqueue? (not/c mqueue-empty?)))
  
(define (mqueue-make)
  (mqueue null null))

(define (mqueue-push q x)
  (define p (mcons x null))
  (if (mqueue-empty? q)
      (set-mqueue-front! q p)
      (set-mcdr! (mqueue-back q) p))
  (set-mqueue-back! q p))

(define ex(mqueue-make))
(mqueue-push ex 3)
(mqueue-push ex 4)
(mqueue-push ex 5)
(mqueue-push ex 6)
(define (drukowanie kol pom)
  (cond
    [(mqueue-empty? kol) pom]
    [(