#!/usr/bin/env racket
#lang racket
(require test-engine/racket-tests)

(* 3 (+ 1 2))

(define (return x)
  x)

(define (k+ a b k)
  (k (+ a b)))

(define (k* a b k)
  (k (* a b)))

(k+ 1 2 (lambda (x) (k* x 3 return)))

;;; normal factorial
(define (fact n)
  (if (= n 1) 
      1
      (* n (fact (- n 1)))))

;;; CPS factorial
(define (kfact n k)
  (if (= n 1) 
      (k 1)
      (kfact (- n 1) (lambda (x) (k (* n x))))))

(check-expect (+ 1 1) 2)
(test)
