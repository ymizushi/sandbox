#!/usr/bin/env racket
#lang racket
(require rackunit "rocket.rkt")

(check-equal? (read-all "hoge.txt") "(define hoge (lambda (x) (+ x x)))")
