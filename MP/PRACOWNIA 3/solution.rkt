#lang plait

; komentarze przeklejone z wykladu ilustrują typ abstrakcyjny

(define-type-alias Value Number)

(define (run [s : S-Exp]) : Value
  (error 'run "not implemented"))

(define-type Op
  (mul) (add) (sub) (leq))

(define-type Exp
  (NUM  [n : Number])
  (SYM  [s : Symbol])
  (OP   [e1 : Exp] [op : Op] [e2 : Exp])               ; {e1 Op e2}
  (IF   [e0 : Exp] [e1 : Exp] [e2 : Exp])              ; {ifz e0 then e1 else e2}
  (DEF  [listap : (Listof (Symbol * Exp))] [e1 : Exp]) ; {define {d1 . . . dk} for e}
  (LET  [s : Symbol] [e1 : Exp] [e2 : Exp])            ; {let x be e1 in e2} 
  (FUN  [listas : (Listof Symbol)] [e1 : Exp])         ; {fun f (x1 . . . xl) = e}
  (F [n : Symbol] [listae : (Listof Exp)]))            ; {f (e1 . . . el)}

(define (parse [s : S-Exp]) 
  (cond
    [(s-exp-match? `NUMBER s)
     (NUM (s-exp->number s))]
    [(s-exp-match? `SYMBOL s)
     (SYM (s-exp->symbol s))]
    [(s-exp-match? `(define ((fun SYMBOL (SYMBOL ...) = ANY) ...) for ANY) s) ; {define {d1 . . . dk} for e}
     (parse-define s)]
    [(s-exp-match? `{ANY SYMBOL ANY} s)  ; {e1 Op e2}
     (parse-opG s)]
    [(s-exp-match? `{ifz ANY then ANY else ANY} s) ; {ifz e0 then e1 else e2}
     (parse-if s)]
    [(s-exp-match? `{let SYMBOL be ANY in ANY} s) ; {let x be e1 in e2} 
     (parse-let s)]
    [(s-exp-match? `{SYMBOL (ANY ...)} s)  ; {f (e1 . . . el)}
     (parse-f s)]
    [else (error 'parse "invalid input")]))

(define (parse-define [s : S-Exp]) ; {define {d1 . . . dk} for e}
  (DEF (map parse-func (s-exp->list (list-ref (s-exp->list s) 1)))
    (parse (list-ref (s-exp->list s) 3))))

(define (parse-func [s : S-Exp]) ;{ fun f (x1 . . . xl) = e}
  (pair
     (s-exp->symbol (list-ref (s-exp->list s) 1))
     (FUN
        (map s-exp->symbol (s-exp->list (list-ref (s-exp->list s) 2)))
        (parse (list-ref (s-exp->list s) 4)))))

(define (parse-if [s : S-Exp]) ; {ifz e0 then e1 else e2}
  (IF (parse (list-ref (s-exp->list s) 1))
      (parse (list-ref (s-exp->list s) 3))
      (parse (list-ref (s-exp->list s) 5))))

(define (parse-let [s : S-Exp]) ; {let x be e1 in e2} 
  (LET (s-exp->symbol (list-ref (s-exp->list s) 1))
       (parse (list-ref (s-exp->list s) 3))
       (parse (list-ref (s-exp->list s) 5))))

(define (parse-opG [s : S-Exp]) ; {e1 Op e2}
  (OP (parse (list-ref (s-exp->list s) 0))
      (parse-op (s-exp->symbol (list-ref (s-exp->list s) 1)))    
      (parse (list-ref (s-exp->list s) 2))))

(define (parse-f [s : S-Exp]) ; {f (e1 . . . el)}
  (F (s-exp->symbol (list-ref (s-exp->list s) 0))
     (map parse (s-exp->list (list-ref (s-exp->list s) 1)))))

(define (parse-op [op : Symbol]) : Op 
  (cond
    [(eq? op '*)  (mul)]
    [(eq? op '+)  (add)]
    [(eq? op '-)  (sub)]
    [(eq? op '<=) (leq)]
    [else (error 'parse "wrong operator type")]))

;------------------------------------------------------------------------------------------------------


(parse `{define
         {[fun fact (n) = {ifz n then 1 else {n * {fact ({n - 1})}}}]}
         for
         {fact (5)}})

(parse `{define
        {[fun even (n) = {ifz n then 0 else {odd ({n - 1})}}]
         [fun odd (n) = {ifz n then 42 else {even ({n - 1})}}]}
        for
        {even (1024)}})

(parse `{define
        {[fun gcd (m n) = {ifz n
                               then m
                               else {ifz {m <= n}
                                         then {gcd (m {n - m})}
                                         else {gcd ({m - n} n)}}}]}
        for
        {gcd (81 63)}})

