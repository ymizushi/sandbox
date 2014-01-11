#!/usr/bin/env racket
#lang racket

(define global-env (make-hash))

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

(define (parse str)
  null
  )

(define (atom token)
  null)

(define (token char)
  null)

(define (space? char)
  (if (or (char-whitespace? char) (char=? #\tab char))
    true
    false))

(define (parentheses? c)
  (if (or
        (char=? #\( c)
        (char=? #\) c))
    true
    false))

(define (tokenize str)
  (let ([ip (open-input-string str)])
    (let loop ([tokening ""]
               [before #\nul]
               [tokens `()]
               )
      (let ([c (read-char ip)])
        (if (eof-object? c)
          tokens
          (cond
            [(space? c)
               (if (space? before)
                 (loop "" c tokens)
                 (loop "" ;tokening
                       c ;before
                       (append tokens (list tokening))))] ;tokens
            [(parentheses? c)
               (loop "" c (append tokens (list (string c))))]
            [else
               (loop (string-append tokening (string c)) c tokens)]))))))

;(-main)

(require test-engine/racket-tests)

(check-expect true (parentheses? #\( ))
(check-expect (tokenize "(define hoge 1 )") (list "(" "define" "hoge" "1" ")") )
(test)
