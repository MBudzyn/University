#lang plait

(define-type ( NNF 'v )
  ( nnf-lit [ polarity : Boolean ] [ var : 'v ])
  ( nnf-conj [ l : ( NNF 'v ) ] [ r : ( NNF 'v ) ])
  ( nnf-disj [ l : ( NNF 'v ) ] [ r : ( NNF 'v ) ]))

(define (eval-lit [env : ('v -> Boolean)] [lit : (NNF 'v)])
  (if (nnf-lit-polarity lit)
      (env (nnf-lit-var lit))
      (not (env (nnf-lit-var lit)))))

(define (neg-nnf [dana : (NNF 'v)])
    (cond
      [(nnf-conj? dana) (nnf-disj (neg-nnf (nnf-conj-l dana)) (neg-nnf (nnf-conj-r dana)))]
      [(nnf-disj? dana) (nnf-conj (neg-nnf (nnf-disj-l dana)) (neg-nnf (nnf-disj-r dana)))]
      [else  (nnf-lit (not (nnf-lit-polarity dana)) (nnf-lit-var dana))]))
    
(define (eval-nnf [env : ('v -> Boolean)] [phi : (NNF 'v)])
  (cond
    [(nnf-lit? phi) (eval-lit env phi)]
    [(nnf-conj? phi) (and (eval-nnf env (nnf-conj-l phi)) (eval-nnf env (nnf-conj-r phi)))]
    [(nnf-disj? phi) (or (eval-nnf env (nnf-disj-l phi)) (eval-nnf env (nnf-disj-r phi)))]))



(define (test-eval-nnf [env : ('v -> Boolean)] [phi : (NNF 'v)])
  (and (equal? (eval-nnf env phi) (not (eval-nnf env (neg-nnf phi))))
       (equal? (eval-nnf env phi) (eval-nnf env (neg-nnf (neg-nnf phi))))))

;; przykładowe wywołanie testów
(define (test-all)
  (and (test-eval-nnf (lambda (x) #t) (nnf-lit #t 'x))
       (test-eval-nnf (lambda (x) #f) (nnf-lit #f 'x))
       (test-eval-nnf (lambda (x) #t) (nnf-conj (nnf-lit #t 'x) (nnf-lit #t 'y)))
       (test-eval-nnf (lambda (x) #f) (nnf-conj (nnf-lit #t 'x) (nnf-lit #f 'y)))
       (test-eval-nnf (lambda (x) #f) (nnf-disj (nnf-lit #f 'x) (nnf-lit #f 'y)))
       (test-eval-nnf (lambda (x) #t) (nnf-disj (nnf-lit #f 'x) (nnf-lit #t 'y)))))

(test-all)
