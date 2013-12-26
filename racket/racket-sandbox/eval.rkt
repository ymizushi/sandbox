#!/usr/bin/env racket
#lang racket
(require test-engine/racket-tests)

(define in (open-input-file "sample.rkt"))

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

(define (atom token)
  (if (string->number token)
    (string->number token)
    (string->symbol token)))


(define (eval-n token env)
  (cond
    ([]
     )
    )
  )

(define (eval w)
  (displayln w))

(define (serialize base add)
  (if (eq? add null)
    base
    (begin
      (eval (first add))
      (serialize (cons base (cons (first add) null)) (rest add)))))

(define (all-read in tokening)
  (let [(r (read-string 1 in))]
    (if (eof-object? r)
      true
      (let [(tokened (tokenize r tokening))]
        (if (eq? (second tokened) null)
          null
          (serialize null (second tokened)))
        (all-read in (first tokened))))))
(all-read in null)
