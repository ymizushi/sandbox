#!/usr/bin/env racket
#lang racket
(require test-engine/racket-tests)

(struct figure (x y [z #:auto])
  #:auto-value 0
  #:transparent)

(struct figuri (x y [z #:auto])
  #:auto-value 0
  #:transparent)

(struct mood-procedure (base rating)
    #:property prop:procedure (struct-field-index base))
(define happy+ (mood-procedure add1 10))
(happy+ 2)
(mood-procedure-rating happy+)

(figure? (figure 1 2))
(figuri? (figuri 1 2))

;(figure-y ())

(check-expect (+ 1 1) 2)
(test)
