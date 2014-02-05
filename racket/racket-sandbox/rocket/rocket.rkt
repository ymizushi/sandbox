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

(define (empty? str)
  (if (< 0 (string-length str))
    false
    true))

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
                 (loop "" c (if (empty? tokening)
                              tokens
                              (append tokens (list tokening)))))]
            [(parentheses? c)
               (loop ""
                     c
                     (append tokens (if (empty? tokening)
                                      (list (string c))
                                      (list tokening (string c)))))]
            [else
               (loop (string-append tokening (string c)) c tokens)]))))))

(define (parse str)
  null)

(define (atom token)
  null)

(define (find env token)
  null)

(struct Symbol (str))

(struct Env (dict outer))

(define (init-env params args outer)
  (Env (make-hash (zip params args)) outer))

(define (find-env env var)
  (if (get env var)
    env
    (find outer var))) 
;途中
(define (zip key value)
  (make-hash))

(define (eval token env)
  (cond
    [(Symbol? token) (find env token)]
    [(not (list? token)) token]
    [(string=? "if" (first token))
      (let* ([rest-token (rest token)]
            [test (first rest-token)] 
            [conseq (second rest-token)]
            [alt (third rest-token)])
        (eval (if (eval test env) conseq alt)))]
    [(string=? "set!" (first token))
      (let* ([rest-token (rest token)]
             [var (first rest-token)]
             [exp (second rest-token)])
        (hash-set! (find env var) var (eval exp env)))]
    [(string=? "define" (first token))
      (let* ([rest-token (rest token)]
             [var (first rest-token)]
             [exp (second rest-token)])
        (hash-set! env var (eval exp env)))]

    [(string=? "lambda" (first token))
      (let* ([rest-token (rest token)]
             [vars (first rest-token)]
             [exp (second rest-token)])
        (lambda (args) (eval exp (init-env vars args env))))]

    [(string=? "begin" (first token))
      (let* ([rest-token (rest token)])
        (last (map (lambda (exp) (eval exp env)) rest-token)))]
    [else 
      (let* (
            [exps (map (lambda (exp) (eval exp env)) token)]
            [proc (first exps)])
        (proc exps*))])) 
;(-main)

(require test-engine/racket-tests)

(check-expect true (parentheses? #\( ))
(check-expect (tokenize "(define hoge 1111)") (list "(" "define" "hoge" "1111" ")") )
(check-expect (tokenize "( define hoge 1111 )") (list "(" "define" "hoge" "1111" ")") )
(check-expect (tokenize " ( define hoge 1111 )  ") (list "(" "define" "hoge" "1111" ")") )
(check-expect (tokenize " (define hoge 1111)") (list "(" "define" "hoge" "1111" ")") )
(test)
