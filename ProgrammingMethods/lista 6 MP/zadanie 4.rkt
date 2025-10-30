#lang plait



( define-type ( NNF 'v )
( nnf-lit [ polarity : Boolean ] [ var : 'v ])
( nnf-conj [ l : ( NNF 'v ) ] [ r : ( NNF 'v ) ])
( nnf-disj [ l : ( NNF 'v ) ] [ r : ( NNF 'v ) ]) )

(define (neg-nnf [dana : (NNF 'v)])
    (cond
      [(nnf-conj? dana) (nnf-disj (neg-nnf (nnf-conj-l dana)) (neg-nnf (nnf-conj-r dana)))]
      [(nnf-disj? dana) (nnf-conj (neg-nnf (nnf-disj-l dana)) (neg-nnf (nnf-disj-r dana)))]
      [else  (nnf-lit (not (nnf-lit-polarity dana)) (nnf-lit-var dana))]))
    
                    

   (define nnf-formula
  (nnf-conj
    (nnf-lit #t 'p)
    (nnf-disj
      (nnf-lit #f 'q)
      (nnf-lit #t 'r))))

(neg-nnf nnf-formula)