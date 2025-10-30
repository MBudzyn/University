#lang racket
(require rackunit)
(define-syntax-rule
  (stream-cons v s)
  (cons v (delay s)))

(define stream-car car)

(define (stream-cdr s)
  (force (cdr s)))

(define stream-null null)
(define stream-null? null?)

(define (stream-ref s n)
  (if (= n 0)
      (stream-car s)
      (stream-ref (stream-cdr s) (- n 1))))

(define (stream-enumerate-interval a b)
  (if (> a b)
      stream-null
      (stream-cons a (stream-enumerate-interval (+ a 1) b))))

(define (scale stream mnoznik)
  (stream-cons (* (stream-car stream) mnoznik) (scale (stream-cdr stream) mnoznik)))

(define stream-ones
  (stream-cons 1 stream-ones))

(define (intigersfromn n)
  (stream-cons n (intigersfromn (+ n 1))))

(define (stream-filter p s)
  (if (stream-null? s)
      stream-null
      (if (p (stream-car s))
          (stream-cons (stream-car s)
                       (stream-filter p (stream-cdr s)))
          (stream-filter p (stream-cdr s)))))

(define (prime? n)
  (cond
    [(= n 1) #f]
    [(= n 2) #t]
    [else
     (define (potega n d)
       (cond
         [(> (* d d) n) #t]
         [(= (modulo n d) 0) #f]
         [else (potega n (+ d 1))]))
     (potega n 2)]))



(define (stream-second-prime-in-interval a b)
  (stream-car
   (stream-cdr
    (stream-filter prime?
                   (stream-enumerate-interval a b)))))

(define (map2 f xs ys)
  (stream-cons
   (f (stream-car xs)
      (stream-car ys))
   (map2 f (stream-cdr xs) (stream-cdr ys))))

(define nats2 (stream-cons 1 (map2 + nats2 stream-ones )))


(define fibs
  (stream-cons 0 (stream-cons 1 (map2 + fibs (stream-cdr fibs))))) 
(define pado
  (stream-cons 1 (stream-cons 1 (stream-cons 1 (map2 +  pado (stream-cdr pado))))))
;--------------------------------------------------- zadanie3
(define silnia
  (stream-cons 1 (map2 * silnia nats2)))

;--------------------------------------------------- zadanie4
(define (partials strumien)
  (stream-cons (stream-car strumien) (map2 + (partials strumien) strumien)))
;-----------------------------------------------------------------

(stream-second-prime-in-interval 18 39)


(stream-ref (stream-enumerate-interval 3 8) 4)
(stream-ref stream-ones 100001)
(stream-ref (intigersfromn 4) 100001)
(stream-ref nats2 5)
(stream-ref fibs 7)
(stream-ref (partials stream-ones ) 5)
(stream-ref (scale stream-ones 7) 1234)

(define (square n)
  (* n n))
(define (divides? d a)
  (if (= (modulo a d) 0) #t #f))
;-----------------------------------------------------Zadanie 2
(define (my-prime? a)
  (define (my-prime-loop a s)
    (let ([d (stream-car s)])
      (if (< a (square d))
          #t
          (and
             (not (divides? d a))
             (my-prime-loop a (stream-cdr s))))))
  (my-prime-loop a my-primes))

(define my-primes
  (stream-cons 2 (stream-filter my-prime? (intigersfromn 3))))
;----------------------------------------------------------------------------

(stream-ref my-primes 7)
(stream-ref pado 6)

(define (integers-from n)
  (stream-cons n (integers-from (+ n 1))))

(define nats (integers-from 0))

;zadanie 5-------------------------------------------------------------------------------------------------

(define (merge s t)
  (let ([scar (stream-car s)]
        [tcar (stream-car t)]
        )
  (cond
    [(= scar tcar) (stream-cons scar (merge (stream-cdr s) (stream-cdr t)))]
    [(< scar tcar) (stream-cons scar (merge (stream-cdr s) t))] 
    [(> scar tcar) (stream-cons tcar (merge s (stream-cdr t)))] 
    ))
  )



(define (ham)
  (letrec (
           [s2 (stream-cons 2 (merge (scale s2 2) (merge (scale s2 3) (scale s2 5))))] 
           [s3 (stream-cons 3 (merge (scale s3 2) (merge (scale s3 3) (scale s3 5))))]
           [s5 (stream-cons 5 (merge (scale s5 2) (merge (scale s5 3) (scale s5 5))))]
           )
    (merge s2 (merge s3 s5)) 
    )
  )

(stream-ref (ham) 5)
