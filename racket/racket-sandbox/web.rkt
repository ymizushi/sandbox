#!/usr/bin/env racket
#lang web-server/insta
(require test-engine/racket-tests)
(require web-server/formlets
         "model-3.rkt")
 
; start: request -> doesn't return
; Consumes a request and produces a page that displays
; all of the web content.
(define (start request)
  (render-blog-page
   (initialize-blog!
    (build-path (current-directory)
                "the-blog-data.sqlite"))
   request))
 
; new-post-formlet : formlet (values string? string?)
; A formlet for requesting a title and body of a post
(define new-post-formlet
  (formlet
   (#%# ,{input-string . => . title}
        ,{input-string . => . body})
   (values title body)))
 
; render-blog-page: blog request -> doesn't return
; Produces an HTML page of the content of the
; blog.
(define (render-blog-page a-blog request)
  (local [(define (response-generator embed/url)
            (response/xexpr
             `(html (head (title "My Blog"))
                    (body
                     (h1 "My Blog")
                     ,(render-posts a-blog embed/url)
                     (form ([action
                             ,(embed/url insert-post-handler)])
                           ,@(formlet-display new-post-formlet)
                           (input ([type "submit"])))))))
 
          (define (insert-post-handler request)
            (define-values (title body)
              (formlet-process new-post-formlet request))
            (blog-insert-post! a-blog title body)
            (render-blog-page a-blog (redirect/get)))]
 
    (send/suspend/dispatch response-generator)))
 
; new-comment-formlet : formlet string
; A formlet for requesting a comment
(define new-comment-formlet
  input-string)
 
; render-post-detail-page: post request -> doesn't return
; Consumes a post and produces a detail page of the post.
; The user will be able to either insert new comments
; or go back to render-blog-page.
(define (render-post-detail-page a-blog a-post request)
  (local [(define (response-generator embed/url)
            (response/xexpr
             `(html (head (title "Post Details"))
                    (body
                     (h1 "Post Details")
                     (h2 ,(post-title a-post))
                     (p ,(post-body a-post))
                     ,(render-as-itemized-list
                       (post-comments a-post))
                     (form ([action
                             ,(embed/url insert-comment-handler)])
                           ,@(formlet-display new-comment-formlet)
                           (input ([type "submit"])))
                     (a ([href ,(embed/url back-handler)])
                        "Back to the blog")))))
 
          (define (insert-comment-handler request)
            (render-confirm-add-comment-page
             a-blog
             (formlet-process new-comment-formlet request)
             a-post
             request))
 
          (define (back-handler request)
            (render-blog-page a-blog request))]
 
    (send/suspend/dispatch response-generator))) 
