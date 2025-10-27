#lang plait

(define-type OP
  (op-add )
  (op-mul)
  (op-div)
  (op-sub))

(define-type Exp
  (exp-number [n : Number])
  (exp-exp [op : OP] [lewa : Exp] [prawa : Exp]))