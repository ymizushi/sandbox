#!/usr/bin/env racket
#lang racket
(require test-engine/racket-tests)

(struct figure (x y [z #:auto])
  #:auto-value 0
  #:transparent)

(struct mood-procedure (base rating)
    #:property prop:procedure (struct-field-index base))
(define happy+ (mood-procedure add1 10))
(happy+ 2)

(mood-procedure-rating happy+)

(figure? (figure 1 2))

(struct square (x y width height))
(define sq1 (square 1 2 3 4))

(check-expect (square-x sq1) 1)
(check-expect (square-y sq1) 2)
(check-expect (square-width sq1) 3)
(check-expect (square-height sq1) 4)

(check-expect (+ 1 1) 2)
(test)
