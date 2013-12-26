#!/usr/bin/env racket
#lang racket
(require test-engine/racket-tests)
(require racket/class)

(define file-interface<%>
  (interface () open close read-byte write-byte))
(define directory-interface<%>
  (interface (file-interface<%>)
    [file-list (->m (listof (is-a?/c file-interface<%>)))]
    parent-directory))
