#! /usr/bin/env racket
#lang racket
;(printf "Given arguments: ~s\n"
;  (current-command-line-arguments))

(define verbose? (make-parameter #f))

(define greeting
  (command-line
    #:once-each
    [("-v") "Verbose mode" (verbose? #t)]
    #:args
    (str) str))
(printf "~a~a\n"
  greeting
  (if (verbose?) " to you, too!" ""))
