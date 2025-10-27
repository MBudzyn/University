#lang plait

(define-type PairListES
  [empty]
  [pair (first : Expr) (second : Symbol) (rest : PairListES)])

(define-type PairListEE
  [empty2]
  [pair2 (first : Expr) (second : Expr) (rest : PairListEE)])

(define-type Expr
  (expr-num [value : Number])
  (expr-var [name : Symbol])
  (expr-lambda [params : (Listof Symbol)] [body : Expr])
  (expr-app [rator : Expr] [rands : (Listof Expr)])
  (expr-if [test : Expr] [left : Expr] [right : Expr])
  (expr-let [ bindings : PairListES] [body : Expr])
  (expr-cond [clauses : PairListEE] [else : Expr]))
