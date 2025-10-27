#lang racket
(require data/heap)
(provide sim? wire?
         (contract-out
          [make-sim        (-> sim?)]
          [sim-wait!       (-> sim? positive? void?)]
          [sim-time        (-> sim? real?)]
          [sim-add-action! (-> sim? positive? (-> any/c) void?)]

          [make-wire       (-> sim? wire?)]
          [wire-on-change! (-> wire? (-> any/c) void?)]
          [wire-value      (-> wire? boolean?)]
          [wire-set!       (-> wire? boolean? void?)]

          [bus-value (-> (listof wire?) natural?)]
          [bus-set!  (-> (listof wire?) natural? void?)]

          [gate-not  (-> wire? wire? void?)]
          [gate-and  (-> wire? wire? wire? void?)]
          [gate-nand (-> wire? wire? wire? void?)]
          [gate-or   (-> wire? wire? wire? void?)]
          [gate-nor  (-> wire? wire? wire? void?)]
          [gate-xor  (-> wire? wire? wire? void?)]

          [wire-not  (-> wire? wire?)]
          [wire-and  (-> wire? wire? wire?)]
          [wire-nand (-> wire? wire? wire?)]
          [wire-or   (-> wire? wire? wire?)]
          [wire-nor  (-> wire? wire? wire?)]
          [wire-xor  (-> wire? wire? wire?)]

          [flip-flop (-> wire? wire? wire? void?)]))

;pomocnicze funkcje logiczne-------------------------------------------------------

(define (nand jeden dwa)
  (not (and jeden dwa)))

(define (nor jeden dwa)
  (not (or jeden dwa)))

(define (xor jeden dwa)
  (not (eq? jeden dwa)))

;porownanieheap--------------------------------------------------------------------
(struct event_in_heap (event time))

(define (first_event_in_heap event1 event2)
   (< (event_in_heap-time event1) (event_in_heap-time event2)))

;symulacja---------------------------------------------------------------------

(struct sim (czas kolejka) #:mutable)

(define (make-sim)
  (sim 0 (make-heap first_event_in_heap)))

(define (sim-wait! sim1 czas)
  (let ([koniec (+ czas (sim-time sim1))])
  (define (rek)
    (when (not (eq? (heap-count (sim-kolejka sim1)) 0))
      (let* ([element (heap-min (sim-kolejka sim1))]
             [element-t (event_in_heap-time element)]
             [element-a (event_in_heap-event element)])
          (when (<= element-t koniec)
            (begin (heap-remove-min! (sim-kolejka sim1))
               (set-sim-czas! sim1 element-t)
               (element-a)
               (rek))))))
  (begin (rek) (set-sim-czas! sim1 koniec))))

 
; co trzeba zrobic : sprawdz czy kolejka pusta jesli tak wyjdz w przeciwnym razie sprawdz czy najmniejsze wydarzenie moze sie wykonac jesli tak wykonaj + usun je z listy nastepnie zaaktualizuj kolejke i wykonaj raz jeszcze 
  

(define (sim-time sim) ; sprawdzone
  (sim-czas sim))


;dodaje do kolejki podane symulacji obiekt typu event_in_heap z wartosciami podanej akcji oraz z czasem = aktualny czas symulacji+opoznienie
(define (sim-add-action! simz opoznienie lambda)
  (let([ev_in_heap
    (event_in_heap
      lambda
      (+ (sim-czas simz) opoznienie))])
  (heap-add! (sim-kolejka simz) ev_in_heap)))

;---------------------------------

(define (drukowaniekolejki heap1 wynik)
  (cond [(not (= (heap-count heap1) 0))
      (heap-remove-min! heap1)])
  (if (= (heap-count heap1) 0)
      wynik
      (drukowaniekolejki heap1 (cons (event_in_heap-time (heap-min heap1)) wynik))))

;kable--------------------------------------------------------------------------

(struct wire (stan symulacja list_of_actions) #:mutable)

(define (make-wire sim1)
  (wire #f sim1 '()))

  
(define (add-all-actions wire12)
  (let ([actions (wire-list_of_actions wire12)]
        [symulacja (wire-symulacja wire12)])
    (for-each
      (lambda (akcja)
        (sim-add-action! symulacja (cdr akcja) (car akcja)))
      actions))) 
        

(define (wire-set! wire1 nowystan)
  (cond [(not (eq? (wire-stan wire1) nowystan)) (add-all-actions wire1)])
  (set-wire-stan! wire1 nowystan))

(define (wire-on-change! wire1 akcja) ; akcja to para skladajaca sie z akcji do wykonania oraz opoznienia
  (set-wire-list_of_actions!
      wire1
     (cons
        akcja
        (wire-list_of_actions wire1)))
  ((car akcja))) 

(define (wire-value wire)
  (wire-stan wire))



;kablecd(logiczne)----------------------------------------------------

(define (wire-not wire1)
  (define nowy (make-wire (wire-symulacja wire1)))
  (gate-not nowy wire1)
   nowy)

(define (wire-nand wire1 wire2)
  (define nowy (make-wire (wire-symulacja wire1)))
  (gate-nand nowy wire1 wire2)
  nowy)

(define (wire-and wire1 wire2)
  (define nowy (make-wire (wire-symulacja wire1)))
  (gate-and nowy wire1 wire2)
   nowy)

(define (wire-or wire1 wire2)
  (define nowy (make-wire (wire-symulacja wire1)))
  (gate-or nowy wire1 wire2)
  nowy)

(define (wire-nor wire1 wire2)
  (define nowy (make-wire (wire-symulacja wire1)))
  (gate-nor nowy wire1 wire2)
  nowy)

(define (wire-xor wire1 wire2)
  (define nowy (make-wire (wire-symulacja wire1)))
  (gate-xor nowy wire1 wire2)
  nowy)


;bramki----------------------------------------------------------------------------------



(define (gate-not wirewyjscie wire2) ; brak obslugi roznych kabli (wywalania errora)
  (if
     (eq? (wire-symulacja wirewyjscie) (wire-symulacja wire2))
     (wire-on-change! wire2 (lambda () (wire-set! wirewyjscie (not (wire-value wire2)))))
     (error "rozne symulacje")))

(define (gate-and wirewyjscie wire2 wire3)
    (cond [(nand (eq? (wire-symulacja wire2) (wire-symulacja wire3)) (eq? (wire-symulacja wire2) (wire-symulacja wirewyjscie))) (error "zle kable")])
    (wire-on-change! wire2 (cons (lambda () (wire-set! wirewyjscie (and (wire-value wire2) (wire-value wire3)))) 1))
    (wire-on-change! wire3 (cons (lambda () (wire-set! wirewyjscie (and (wire-value wire2) (wire-value wire3)))) 1)))
     
(define (gate-nand wirewyjscie wire2 wire3)
    (cond [(nand (eq? (wire-symulacja wire2) (wire-symulacja wire3)) (eq? (wire-symulacja wire2) (wire-symulacja wirewyjscie))) (error "zle kable")])
    (wire-on-change! wire2 (cons (lambda () (wire-set! wirewyjscie (nand (wire-value wire2) (wire-value wire3)))) 1))
    (wire-on-change! wire3 (cons (lambda () (wire-set! wirewyjscie (nand (wire-value wire2) (wire-value wire3)))) 1)))
    

(define (gate-or wirewyjscie wire2 wire3)
     (cond [(nand (eq? (wire-symulacja wire2) (wire-symulacja wire3)) (eq? (wire-symulacja wire2) (wire-symulacja wirewyjscie))) (error "zle kable")])
     (wire-on-change! wire2 (cons (lambda () (wire-set! wirewyjscie (or (wire-value wire2) (wire-value wire3)))) 1))
     (wire-on-change! wire3 (cons (lambda () (wire-set! wirewyjscie (or (wire-value wire2) (wire-value wire3))))) 1))
    

(define (gate-xor wirewyjscie wire2 wire3)
    (cond [(nand (eq? (wire-symulacja wire2) (wire-symulacja wire3)) (eq? (wire-symulacja wire2) (wire-symulacja wirewyjscie))) (error "zle kable")])
    (wire-on-change! wire2 (cons (lambda () (wire-set! wirewyjscie (xor (wire-value wire2) (wire-value wire3)))) 2))
    (wire-on-change! wire3 (cons (lambda () (wire-set! wirewyjscie (xor (wire-value wire2) (wire-value wire3)))) 2)))


(define (gate-nor wirewyjscie wire2 wire3)
    (cond [(nand (eq? (wire-symulacja wire2) (wire-symulacja wire3)) (eq? (wire-symulacja wire2) (wire-symulacja wirewyjscie))) (error "zle kable")])
    (wire-on-change! wire2 (cons (lambda () (wire-set! wirewyjscie (nor (wire-value wire2) (wire-value wire3)))) 1))
    (wire-on-change! wire3 (cons (lambda () (wire-set! wirewyjscie (nor (wire-value wire2) (wire-value wire3))))) 1))

;------------------------------------------------------------------------------------------------------


            
(define (bus-value ws)
  (foldr (lambda (w value) (+ (if (wire-value w) 1 0) (* 2 value)))
         0
         ws))

(define (bus-set! wires value)
  (match wires
    ['() (void)]
    [(cons w wires)
     (begin
       (wire-set! w (= (modulo value 2) 1))
       (bus-set! wires (quotient value 2)))]))


(define (flip-flop out clk data)
  (define sim (wire-symulacja data))
  (define w1  (make-wire sim))
  (define w2  (make-wire sim))
  (define w3  (wire-nand (wire-and w1 clk) w2))
  (gate-nand w1 clk (wire-nand w2 w1))
  (gate-nand w2 w3 data)
  (gate-nand out w1 (wire-nand out w3)))


(define sim3 (make-sim))
(define sim2 (make-sim))

(define (make-counter n clk en)
  (if (= n 0)
      '()
      (let [(out (make-wire sim3))]
        (flip-flop out clk (wire-xor en out))
        (cons out (make-counter (- n 1) clk (wire-and en out))))))

(define clk (make-wire sim3))
(define en  (make-wire sim3))
(define counter (make-counter 4 clk en))

(wire-set! en #t)

(define (tick)
  (wire-set! clk #t)
  (sim-wait! sim3 20)
  (wire-set! clk #f)
  (sim-wait! sim3 20)
  (bus-value counter))


(tick)
(tick)
(tick)
(tick)
(tick)
(tick)
(tick)
(tick)
(tick)
