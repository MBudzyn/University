#lang plait

(define-type (2-3 'a)
  (leaf2)
  (node2 [l : (2-3 'a)] [elem : 'a] [r : (2-3 'a)])
  (node3 [l : (2-3 'a)] [elema : 'a] [s : (2-3 'a)] [elemb : 'a] [r : (2-3'a)]))

(define (wieksza a b)
  (if (> a b) a b))
(define (mniejsza a b)
  (if (< a b) a b))

(define (height-23tree tree w)
  (type-case (2-3 'a) tree
    [(leaf2)  w]
    [(node2 l e r)
     (wieksza
      (height-23tree l (+ w 1))
      (height-23tree r (+ w 1)))]
    [(node3 l e1 s e2 r)
     (wieksza
     (height-23tree l (+ w 1))
     (wieksza
        (height-23tree s (+ w 1))
        (height-23tree r (+ w 1))))]))
  
(define (maksv t [zmienna : 'a])
  (type-case (2-3 'a) t
    [(leaf2) zmienna]
    [(node2 l a r)
     (if (> a zmienna)
         (wieksza
           (maksv (node2-l t) a)
           (maksv (node2-r t) a))
         (wieksza
           (maksv (node2-l t) zmienna)
           (maksv (node2-r t) zmienna)))]
    [(node3 l a s b r)
    (if (> (wieksza a b) zmienna)
        (wieksza
           (wieksza 
               (maksv (node3-l t) (wieksza a b))
               (maksv (node3-s t) (wieksza a b)))
           (maksv (node3-r t) (wieksza a b)))
        (wieksza
           (wieksza 
               (maksv (node3-l t) zmienna)
               (maksv (node3-s t) zmienna))
           (maksv (node3-r t) zmienna)))]))

(define (minv t [zmienna : 'a])
  (type-case (2-3 'a) t
    [(leaf2) zmienna]
    [(node2 l a r)
     (if (< a zmienna)
         (mniejsza
           (minv (node2-l t) a)
           (minv (node2-r t) a))
         (mniejsza
           (minv (node2-l t) zmienna)
           (minv (node2-r t) zmienna)))]
    [(node3 l a s b r)
    (if (< (mniejsza a b) zmienna)
        (mniejsza
           (mniejsza
               (minv (node3-l t) (mniejsza a b))
               (minv (node3-s t) (mniejsza a b)))
           (minv (node3-r t) (mniejsza a b)))
        (mniejsza
           (mniejsza 
               (minv (node3-l t) zmienna)
               (minv (node3-s t) zmienna))
           (minv (node3-r t) zmienna)))]))

(define (czy2-3 t)
  (type-case (2-3 'a) t
    [(leaf2) #t]
    [(node2 l elem r)
     (and
      (= (height-23tree l 0) (height-23tree r 0))
      (> elem (maksv l -inf.0))
      (< elem (minv r +inf.0))
      (czy2-3 l)
      (czy2-3 r))]
     [(node3 l elema s elemb r)
     (and
      (> elema elemb)
      (> elemb (maksv l -inf.0))
      (< elema (minv r +inf.0))
      (if (leaf2? s)
          #t
         (and
         (> elema (maksv s -inf.0))
         (< elemb (maksv s -inf.0))
         (> elema (minv s +inf.0))
         (< elemb (minv s +inf.0))))
      (= (height-23tree l 0) (height-23tree r 0))
      (= (height-23tree l 0) (height-23tree s 0))
      (= (height-23tree s 0) (height-23tree r 0))
      (czy2-3 l)
      (czy2-3 r)
      (czy2-3 s))]))
          
        
           
           
(define przykladowe
         (node2 (leaf2) 21
                (node3 (leaf2) 35 (leaf2) 22
                       (node2
                          (node2 (leaf2) 40 (leaf2))
                          45
                          (node3 (leaf2) 71 (leaf2) 70 (leaf2))))))

(define przykladowe2 (node2 (node2 (leaf2) 4 (leaf2)) 10 (leaf2)))
                

(maksv (leaf2) -inf.0)

(minv (leaf2) +inf.0)
         
(czy2-3 przykladowe)
(height-23tree przykladowe 0)
  
