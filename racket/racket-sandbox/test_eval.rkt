#!/usr/bin/env racket
#lang racket
(require rackunit "eval.rkt")

(check-equal? (tokenizer "a" "") (list true"a") "simple tokenize")
