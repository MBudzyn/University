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

(struct sim (time kolejka) #:mutable)

(define (make-sim)
  (sim 0 (make-heap first_event_in_heap)))

  
(define (sim-wait! sim1 opoznienie)
  (set-sim-time! sim1 (+ (sim-time sim1) opoznienie)))
 

; co trzeba zrobic : sprawdz czy kolejka pusta jesli tak wyjdz w przeciwnym razie sprawdz czy najmniejsze wydarzenie moze sie wykonac jesli tak wykonaj + usun je z listy nastepnie zaaktualizuj kolejke i wykonaj raz jeszcze 
  

(define (sim-time1 sim)
  (sim-time sim))

(define (sim-add-action! sim1 opoznienie lambda)
  (define ev_in_heap
    (event_in_heap
      lambda
      (+ (sim-time sim1) opoznienie)))
  (heap-add! (sim-kolejka sim1) ev_in_heap))

;kable--------------------------------------------------------------------------

(struct wire (stan symulacja list_of_actions) #:mutable)

(define (make-wire sim)
  (wire #f sim '()))

(define (wire-set!-wire new_mod_wire wire)
  (wire-set! new_mod_wire (wire-stan wire)))

(define (wire-set! wire nowystan)
  (set-wire-stan! wire nowystan))

(define (wire-on-change! wire1 akcja)
  (set-wire-list_of_actions!
      wire1
     (cons
        (event_in_heap (car akcja) (cdr akcja))
        (wire-list_of_actions wire1)))) ; dodanie akcji z wywolaniem bez sprawdzenia czy dziala

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
  (gate-and (nowy wire1 wire2))
   nowy)

(define (wire-or wire1 wire2)
  (define nowy (make-wire (wire-symulacja wire1)))
  (gate-or (nowy wire1 wire2))
  nowy)

(define (wire-nor wire1 wire2)
  (define nowy (make-wire (wire-symulacja wire1)))
  (gate-nor (nowy wire1 wire2))
  nowy)

(define (wire-xor wire1 wire2)
  (define nowy (make-wire (wire-symulacja wire1)))
  (gate-xor (nowy wire1 wire2))
  nowy)


;bramki----------------------------------------------------------------------------------



(define (gate-not wirewyjscie wire2) ; brak obslugi roznych kabli (wywalania errora)
  (if
     (eq? (wire-symulacja wirewyjscie) (wire-symulacja wire2))
     (wire-on-change! wire2 (lambda () (wire-set! wirewyjscie (not (wire-value wire2)))))
     (error "rozne symulacje")))

(define (gate-and wirewyjscie wire2 wire3)
    (wire-on-change! wire2 (cons (lambda () (wire-set! wirewyjscie (and (wire-value wire2) (wire-value wire3)))) 1))
    (wire-on-change! wire3 (cons (lambda () (wire-set! wirewyjscie (and (wire-value wire2) (wire-value wire3))))) 1))
     
(define (gate-nand wirewyjscie wire2 wire3)
    (wire-on-change! wire2 (cons (lambda () (wire-set! wirewyjscie (nand (wire-value wire2) (wire-value wire3)))) 1 ))
    (wire-on-change! wire3 (cons (lambda () (wire-set! wirewyjscie (nand (wire-value wire2) (wire-value wire3)))) 1)))
    

(define (gate-or wirewyjscie wire2 wire3)
     (wire-on-change! wire2 (lambda () (wire-set! wirewyjscie (or (wire-value wire2) (wire-value wire3)))))
     (wire-on-change! wire3 (lambda () (wire-set! wirewyjscie (or (wire-value wire2) (wire-value wire3))))))
    

(define (gate-xor wirewyjscie wire2 wire3)
    (wire-on-change! wire2 (lambda () (wire-set! wirewyjscie (xor (wire-value wire2) (wire-value wire3)))))
    (wire-on-change! wire3 (lambda () (wire-set! wirewyjscie (xor (wire-value wire2) (wire-value wire3))))))


(define (gate-nor wirewyjscie wire2 wire3)
    (wire-on-change! wire2 (lambda () (wire-set! wirewyjscie (nor (wire-value wire2) (wire-value wire3)))))
    (wire-on-change! wire3 (lambda () (wire-set! wirewyjscie (nor (wire-value wire2) (wire-value wire3))))))


            
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

;testy------------------------------------------------------------------
(define sim1 (make-sim))
(define sim2 (make-sim))
(define wire1 (make-wire sim1))
(wire-set! wire1 #t)

(wire-stan wire1)
(define wire2 (make-wire sim1))
(wire-set! wire2 #t)
(define wire22 (make-wire sim2 ))
(define wire3 (make-wire sim1))
;(define g1 (gate-not wire1 wire2))
;(define g2 (gate-not wire1 wire2))

(heap-count (sim-kolejka sim1))
;(pretty-print (car(wire-list_of_actions wire2)))
(define wire4 (wire-nand wire1 wire2))
(wire-set!-wire wire1 wire2)
(wire-stan wire1)
(define wire5 (wire-nand wire1 wire2))
;(define wire6 (wire-nand wire1 wire22))
(sim-add-action! sim1 3 (lambda () (displayln "Akcja!")))
(sim-add-action! sim1 4 (lambda () (displayln "Akcja!")))
(sim-add-action! sim1 2 (lambda () (displayln "Akcja!")))
(heap-count (sim-kolejka sim1))


;lista lambd-------------------------------------------
(define funkcje
  (list
    (lambda () (display "Funkcja 1\n"))
    (lambda () (display "Funkcja 2\n"))
    (lambda () (display "Funkcja 3\n"))))

((car funkcje)) ; Wywołanie pierwszej funkcji anonimowej z listy