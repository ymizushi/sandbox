#!/usr/bin/env racket
#lang racket

(define (read-all file-name)
  (let ([in (open-input-file file-name)])
    (let loop ([buffer ""])
      (let ([c (read-string 1 in)])
        (if (eof-object? c)
          (begin 
            (close-input-port in)
            buffer)
          (loop (string-append buffer c)))))))

(define (write-file str filename)
  (let ([out (open-output-file "output.txt" #:exists 'append)])
    (begin
      (write str out)
      (close-output-port out))))

(define (-main)
  (if (= 0 (vector-length (current-command-line-arguments)))
    (begin 
      (displayln "no argment")
      (read-all "sample.rkt"))
    (read-all (vector-ref (current-command-line-arguments) 0))))

(define (tokenize r tokening)
  (cond
    [(string=? r "(")
       (list null (list "("))]
    [(string=? r ")")
       (if (eq? tokening null)
         (list null (list ")"))
         (list null (list tokening ")")))]
    [(or (string=? r " ") (string=? r "\n"))
       (if (eq? tokening null)
         (list null null)
         (list null (list tokening)))]
    [else
       (if (eq? tokening null)
         (list r null)
         (list (string-append tokening r) null))]))

(-main)

(require test-engine/racket-tests)
(test)
