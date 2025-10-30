#lang racket

( define ( foldl-map f a xs )
  (parametric->/c [ a b c] (-> (-> a b c) b ( listof a) (pair? (listof c) c )))
   ( define ( it a xs ys )
      (if ( null? xs )
          ( cons ( reverse ys ) a )
          (let [( p ( f ( car xs ) a ) ) ]
            ( it ( cdr p )
                 ( cdr xs )
                 ( cons ( car p ) ys ) ) ) ) )
   ( it a xs null ) )


;(foldl-map + 0 (list 1 2 3 4))
( foldl-map ( lambda ( x a ) ( cons a (+ a x ) ) ) 0 (list 1 2) )
