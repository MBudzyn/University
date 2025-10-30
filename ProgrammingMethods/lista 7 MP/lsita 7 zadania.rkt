#lang plait


(define-type (Tree 'a)
  (leaf)
  (node2 [l : (Tree 'a)] [elem : 'a] [r : (Tree 'a)])
  (node3 [l : (Tree 'a)] [elema : 'a] [s : (Tree 'a)] [elemb : 'a] [r : (Tree 'a)]))

(define (insert x t)
  (type-case (Tree 'a) t
    [(leaf) (node2 (leaf) x (leaf))]
    [(node2 l y r)
     (if (< x y)
         (node2 (insert x l) y r)
         (node2 l y (insert x r)))]
    [(node3 l a s b r) (leaf)]))


  (define (check-node2 node)
    (and (<= (node2-elem node) (tree-max (node2-left node)))
         (<= (node2-elem node) (tree-min (node2-right node)))
         (check-2-3-tree (node2-left node))
         (check-2-3-tree (node2-right node))))
  
  (define (check-node3 node)
    (and (<= (node3-elema node) (node3-elemb node))
         (<= (node3-elema node) (tree-max (node3-left node)))
         (<= (node3-elema node) (tree-min (node3-s node)))
         (<= (node3-elemb node) (tree-max (node3-s node)))
         (<= (node3-elemb node) (tree-min (node3-right node)))
         (check-2-3-tree (node3-left node))
         (check-2-3-tree (node3-s node))
         (check-2-3-tree (node3-right node))))

  (type-case Tree t
    [(leaf) #t]
    [(node2 l elem r) (and (check-node2 (make-node2 l elem r)) #t)]
    [(node3 l elema s elemb r) (and (check-node3 (make-node3 l elema s elemb r)) #t)])
