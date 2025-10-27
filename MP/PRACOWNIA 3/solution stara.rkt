#lang plait

(define-type-alias Value Number)

(define (run [s : S-Exp]) : Value
  (error 'run "not implemented"))

(define-type Op
  (mul) (sub) (add) (leq)) ; zamieniona kolejnosc

(define-type Exp
  (numE [n : Number])
  (varE [v : Symbol])
  (opE [op : Op] [e1 : Exp] [e2 : Exp])
  (defE [listap : (Listof (Symbol * Exp))] [e1 : Exp])
  (ifE [condition : Exp] [e1 : Exp] [e2 : Exp])
  (letE [v : Symbol] [e1 : Exp] [e2 : Exp])
  (funE [listas : (Listof Symbol)] [e1 : Exp])
  (appE [n : Symbol] [listae : (Listof Exp)]))

(define (parse-func [s : S-Exp])
  (pair
   (s-exp->symbol (second (s-exp->list s)))
   (funE
    (map s-exp->symbol (s-exp->list (third (s-exp->list s))))
    (parse-exp (fourth (rest (s-exp->list s)))))))

(define (parse-define [s : S-Exp])
  (defE (map parse-func (s-exp->list (second (s-exp->list s))))
    (parse-exp (fourth (s-exp->list s)))))

(define (parse-exp [s : S-Exp]) ; nic nie zmienione
  (cond
    [(s-exp-match? `NUMBER s)
     (numE (s-exp->number s))]
    [(s-exp-match? `SYMBOL s)
     (varE (s-exp->symbol s))]
    [(s-exp-match? `{ANY SYMBOL ANY} s)
     (parse-opG s)]
    [(s-exp-match? `{ifz ANY then ANY else ANY} s)
     (parse-if s)]
    [(s-exp-match? `{let SYMBOL be ANY in ANY} s)
     (parse-let s)]
    [(s-exp-match? `{SYMBOL (ANY ...)} s)
     (parse-app s)]
    [else (error 'parse "invalid input")]))

(define (parse-if [s : S-Exp])
  (ifE (parse-exp (second (s-exp->list s)))
       (parse-exp (fourth (s-exp->list s)))
       (parse-exp (fourth (rest (rest (s-exp->list s)))))))

(define (parse-let [s : S-Exp])
  (letE (s-exp->symbol (second (s-exp->list s)))
           (parse-exp (fourth (s-exp->list s)))
           (parse-exp (fourth (rest (rest (s-exp->list s)))))))

(define (parse-opG [s : S-Exp])
  (opE (parse-op (s-exp->symbol (second (s-exp->list s))))
          (parse-exp (first (s-exp->list s)))
          (parse-exp (third (s-exp->list s)))))

(define (parse-app [s : S-Exp])
  (appE (s-exp->symbol (first (s-exp->list s)))
           (map parse-exp (s-exp->list (second (s-exp->list s))))))

(define (parse-op [op : Symbol]) : Op ; nic nie zmienione
  (cond
    [(eq? op '*) (mul)]
    [(eq? op '+) (add)]
    [(eq? op '-) (sub)]
    [(eq? op '<=) (leq)]
    [else (error 'parse "wrong operator type")]))

;------------------------------------------------------------------------------------------------------

(define-type Dane
  (valD [val : Value])
  (funD [xs : (Listof Symbol)] [e : Exp]))

(define-type Binding
  (bind [name : Symbol] [data : Dane]))

(define-type-alias Env (Listof Binding))

(define make-env empty)

(define (extend-env [env : Env] [x : Symbol] [d : Dane]) : Env
  (cons (bind x d) env))

(define (extend-env-list [env : Env] [xs : (Listof (Symbol * Dane))])
  (if (empty? xs)
       env
      (let ([p (first xs)]) (extend-env-list (extend-env env (fst p) (snd p)) (rest xs))))) 
  
(define (lookup-env [n : Symbol] [env : Env])
  (type-case (Listof Binding) env
    [empty (error 'lookup "unbound variable")]
    [(cons b rst-env) (cond
                        [(eq? n (bind-name b)) (bind-data b)]
                        [else (lookup-env n rst-env)])]))

;-------------------------------------------------------------------------------------------
(define (eval [e : Exp] [env : Env])
  (type-case Exp e
    [(numE n)
     (valD n)]
    [(opE op l r)
     (valD (eval-op op (valD-val (eval l env)) (valD-val (eval r env))))]
    [(ifE b l r) (if (= (valD-val (eval b env)) 0) (eval l env) (eval r env))]
    [(varE x) (lookup-env x env)]
    [(letE x e1 e2) (eval e2 (extend-env env x (eval e1 env)))]
    [(funE xs b) (funD xs b)]
    [(appE name es) (apply (lookup-env name env) es env)]
    [(defE fs e)
     (let ([ds (map (lambda (p) (pair (fst p) (eval (snd p) env))) fs)])
       (eval e (extend-env-list env ds)))]))

(define (pair-list lista1 lista2)
  (if (empty? lista1) '()
      (cons (pair (first lista1) (first lista2))
            (pair-list (rest lista1) (rest lista2)))))

(define (apply [f : Dane] [es : (Listof Exp)] [env : Env])
  (let ([d (map (lambda (e) (eval e env)) es)])
  (eval (funD-e f) (extend-env-list env (pair-list (funD-xs f) d)))))
  
(define (eval-op [op : Op] [v1 : Value] [v2 : Value]) : Value
  (type-case Op op
    [(add) (+ v1 v2)]
    [(sub) (- v1 v2)]
    [(mul) (* v1 v2)]
    [(leq) (if (<= v1 v2) 0 42)]))




