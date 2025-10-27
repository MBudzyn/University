#lang plait

(define-type Op
  (op-add) (op-mul) (op-sub) (op-div) (op-pow))

(define-type Op1
  (op-silnia) (op-przeciwna))
; zadeklarowanie abstrakcyjnych metod op

(define-type Exp ; zdefiniowanie typu wyrazenie 
  (exp-number [n : Number])
  (exp-op [op : Op] [e1 : Exp] [e2 : Exp])
  (exp-op1 [op : Op1] [e : Exp]))
  

(define (dl xs)
  (if (empty? (rest xs))
      1
      (+ 1 (dl (rest xs)))))
            
(define (parse-Op s)
  (let ([sym (s-exp->symbol s)])
  (cond
    [(equal? sym '+) (op-add)]
    [(equal? sym '-) (op-sub)]
    [(equal? sym '*) (op-mul)]
    [(equal? sym '/) (op-div)]
    [(equal? sym 'power) (op-pow)])))

(define (parse-Op1 s)
  (let ([sym (s-exp->symbol s)])
  (cond
    [(equal? sym 'silnia) (op-silnia)]
    [(equal? sym 'przeciwna) (op-przeciwna)])))

(define (parse-Exp s)
  (cond
    [(s-exp-number? s) (exp-number (s-exp->number s))]
    [(s-exp-list? s)
     (let ([xs (s-exp->list s)])
       (if (= (dl xs) 3)
       (exp-op (parse-Op  (first  xs))
               (parse-Exp (second xs))
               (parse-Exp (third  xs)))
       (exp-op1 (parse-Op1 (first  xs))
                (parse-Exp (second xs))
             )))]))

(define (parse-Expzadanie4 s)
  (cond
    [(s-exp-number? s) (exp-number (s-exp->number s))]
    [(s-exp-list? s)
     (let ([xs (s-exp->list s)])
       (if (= (dl xs) 3)
       (exp-op (parse-Op  (first  xs))
               (parse-Exp (second xs))
               (parse-Exp (third  xs)))
       (exp-op1 (parse-Op1 (first  xs))
                (parse-Exp (second xs))
             )))]))
        
; ==============================================
(define (power podstawa potega)
 (local
    [(define (it podstawa potega wynik)
      (cond
      [(= potega 0) 1]
      [(= potega 1) (* podstawa wynik)]
      [else (it podstawa (- potega 1) (* wynik podstawa))]))]
    (it podstawa potega 1)))
  
(define (silnia liczba)
 (local
    [(define (it liczba wynik)
      (cond
      [(= liczba 0) 1]
      [(= liczba 1) wynik]
      [else (it (- liczba 1) (* wynik liczba))]))]
    (it liczba 1)))

(define (przeciwna liczba)
  (if (= liczba 0) 0 (* -1 liczba)))


(define (eval-op op)
  (type-case Op op
    [(op-add) +]
    [(op-sub) -]
    [(op-mul) *]
    [(op-div) /]
    [(op-pow) power]))

(define (eval-op1 op)
  (type-case Op1 op
    [(op-silnia) silnia]
    [(op-przeciwna) przeciwna]))

(define (eval e)
  (type-case Exp e
    [(exp-number n)    n]
    [(exp-op op e1 e2)
     ((eval-op op) (eval e1) (eval e2))]
    [(exp-op1 op e1)
     ((eval-op1 op) (eval e1))]))

(define k  (exp-op (op-mul) (exp-number 7) (exp-number 3)))
(eval k)

(define k2 (exp-op1 (op-silnia) (exp-number 4)))
(eval k2)

(eval k)


