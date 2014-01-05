#!/usr/bin/env racket
#lang racket
(require test-engine/racket-tests)

(define fish%
  (class object%
    (init size)                
    (define current-size size)
    (super-new)               
    (define/public (get-size)
      current-size)
    (define/public (grow amt)
      (set! current-size (+ amt current-size)))
    (define/public (eat other-fish)
      (grow (send other-fish get-size)))))

(define hungry-fish%
  (class fish% (super-new)
    (define/public (eat-more fish1 fish2)
      (send this eat fish1)
      (send this eat fish2))))

(define charlie (new fish% [size 10]))

(print (send charlie get-size))
(send charlie grow 6)

(define grower-interface (interface () grow))
(define (picky-mixin %)
  (unless (implementation? % grower-interface)
    (error "picky-mixin: not a grower-interface class")))

(test)
