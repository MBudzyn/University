#lang plait

(define-type Prop
   (var [v : String ])
   (conj [l : Prop ] [r : Prop ])
   (disj [l : Prop ] [r : Prop ])
   (neg [f : Prop ]))

(define (eval [h : (Hashof String Boolean)] [p : Prop])
  (cond
    [(var?  p) (some-v (hash-ref h (var-v p)))]
    [(conj? p) (and (eval h (conj-l p)) (eval h (conj-r p)))]
    [(disj? p) (or (eval h (disj-l p)) (eval h (disj-r p)))]
    [(neg? p) (not (eval h (neg-f p)))]))

(define (tautology? p)
  (all-true? (map (lambda (val) (eval val p)) (make-all-val-hash p)))); podaje do funkcji lambda jako argument hash mape i wszystkich wynikow wartosciowania p i mapuje je do jednej listy a potem sprawdza czy wszystkie zwrocone wartosci sa #t

(define (all-true? l) ; sprawdza czy wszystkie wartosci w liscie sa true
  (local [(define (it l acc)
          (if (empty? l) acc
              (it (rest l) (and acc (first l)))))]
    (it l #t)))

(define (make-all-val-hash p) ; tworzy hash mape w ktorej kluczami sa wszystkie nie  powtarzajace sie zmienne w formule p a wartosciami wszystkie mozliwe wartosciowania tych zmiennych
  (make-hash-list (free-vars p) (all-valuations p)))
  
(define (make-hash-list vars vals) ; tworzy hash mape ktora posiada jako klucze wszystkie pary zmiiennych z lista mozliwych wartosci a wartosci to obliczona wartosc 
  (map (lambda (val) (hash (make-pair-list vars val))) vals))

(define (make-pair-list l1 l2) ; zwraca liste par kazda para zawiera wartosci z dwoch list o  tym samym indeksie
  (local [(define (it l1 l2 nl)
            (if (empty? l1) nl
                (it (rest l1) (rest l2) (cons (pair (first l1) (first l2)) nl))))]
    (it l1 l2 '())))

(define (all-valuations [p : Prop]) ; zwraca liste wszystkich mozliwych wartosciowan zmiennych poprzez zaaplikowanie listy (#t #f) do dlugosi listy o zmiennych bez powtorzen
  (all-variations '(#t #f) (list-len (free-vars p))))

(define (list-len l) ; dlugosc listy iteracyjnie z licznikiem k
  (local [(define (it l k)
          (if (empty? l) k
              (it (rest l) (+ k 1))))]
    (it l 0)))




(define (free-vars [p : Prop] ) ; zwraca liste zmiennych bez powtórzen 
  (no-repeat-list (all-vars p))) ; wywoluje funkcje usuwajaca powtorzenia z argumentem ktory jest funkcja zwracajaca wszystkie wartosciowania p 

(define (no-repeat-list l) ; zwraca liste bez powtorzen
  (local [(define (it l nl)
    (if (empty? l)
        nl
        (it (rest l) (append nl (if (member (first l) nl) '() (list (first l)))))))]
  (it l '())))

(define (all-vars [p : Prop]) ; tworzy  kilkukrote listy listy splaszczane procedura flatten ktore zawieraja wszystkie zmienne p z powtorzeniami
  (cond
    [(var?  p) (list (var-v p))]
    [(conj? p) (flatten (list (all-vars (conj-l p)) (all-vars (conj-r p))))]
    [(disj? p) (flatten (list (all-vars (disj-l p)) (all-vars (disj-r p))))]
    [(neg? p) (flatten (list (all-vars (neg-f p))))]))

(define (flatten lst) ;pozbywa sie kilku zagniezdzonych list prasujac je do listy jednowymiarowej
  (if (empty? lst) '()
      (append (first lst) (flatten (rest lst)))))

(define (all-variations lst k) ;tworzy liste wszystkich kombinacij poprzez zaaplikowanie rekurencyjne jako argument
  (if (<= k 0) '(())
      (flatten (map (lambda (x) (map (lambda (y) (cons x y)) (all-variations lst (- k 1)))) lst))))


(all-variations (list 1 2 ) 4)

(define p1 (conj (disj (var "x") (neg (var "z"))) (var "y"))) ;
(define p2 (disj (neg (var "x")) (var "x"))) ; x | ~x
(define p3 (conj (neg (var "x")) (var "x"))) ; x & ~x
(define p4 (conj
            (disj (neg (var "x")) (var "x"))
            (disj (neg (var "y")) (var "y")))) ; (x | ~x) & (y | ~y)

(tautology? p1)
(tautology? p2)
(tautology? p3)
(tautology? p4)