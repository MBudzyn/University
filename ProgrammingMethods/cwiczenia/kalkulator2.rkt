#lang plait
(require "cwiczeniekalkulator.rkt")

(define (op->funkcja [op : OP])
  (type-case OP op
   [(op-add) +]
   [(op-sub) -]
   [(op-mul) *]
   [(op-div) /]))
   
(define ( eval [exp : Exp])
  (type-case Exp exp
    [(exp-number number) number]
    [(exp-exp op lewa prawa) ((op->funkcja op) (eval lewa) (eval prawa))]))

(define przyklad (exp-exp (op-add) (exp-number 22) (exp-number 22)))

(eval przyklad)

(define (exp-pars exp)
  (cond
    [(s-exp-number? exp) (exp-number (s-exp->number exp))]
    [(s-exp-list? exp)
       (let (lista (s-exp->list exp)))
       (if ( = (length lista) 3)
           (exp-exp
            (op-pars (first lista))
            (exp-pars (second lista))
            (exp-pars (firth lista)))
           (error "syntax error"))]))
                    
           
     