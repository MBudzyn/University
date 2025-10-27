#lang plait

(define-type Prop
   (var [v : String ])
   (conj [l : Prop ] [r : Prop ])
   (disj [l : Prop ] [r : Prop ])
   (neg [f : Prop ]))

(define (eval [h : (Hashof String Boolean)] [p : Prop])
  (cond
    [(var?  p) (some-v (hash-ref h (var-v p)))] ; typ option of some-v aby funkcja zwrocila typ boolean
    [(conj? p) (and (eval h (conj-l p)) (eval h (conj-r p)))]
    [(disj? p) (or (eval h (disj-l p)) (eval h (disj-r p)))]
    [(neg? p) (not (eval h (neg-f p)))]))

