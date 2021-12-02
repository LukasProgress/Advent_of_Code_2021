;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname Day2) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(require 2htdp/batch-io)
(define DATA (read-words/line "data.txt"))
; part 1
; start at 0 0
(define (findPos data)
  (navigate data (make-posn 0 0)))
; navigate according to the data
(define (navigate data pos)
  (let [(amount (lambda (x) (string->number (second x))))]
    (match data
      (empty pos)
      ((cons x xs) (match (first x)
                     ("forward" (navigate xs (make-posn (+ (posn-x pos) (amount x))
                                                        (posn-y pos))))
                     ("down" (navigate xs (make-posn (posn-x pos)
                                                     (+ (posn-y pos) (amount x)))))
                     ("up" (navigate xs (make-posn (posn-x pos)
                                                   (- (posn-y pos) (amount x))))))))))
; create output for the depth data
(define foundPos (findPos DATA))
(* (posn-x foundPos) (posn-y foundPos))

; part 2
; navigate with aim
(define (navigate-with-aim data pos aim)
  (let [(amount (lambda (x) (string->number (second x))))]
    (match data
      (empty pos)
      ((cons x xs) (match (first x)
                     ("forward" (navigate-with-aim xs (make-posn (+ (posn-x pos) (amount x))
                                                        (+ (posn-y pos) (* aim (amount x))))
                                          aim))
                     ("down" (navigate-with-aim xs pos (+ aim (amount x))))
                     ("up" (navigate-with-aim xs pos (- aim (amount x)))))))))
; create output
(define foundPos2 (navigate-with-aim DATA (make-posn 0 0) 0))
(* (posn-x foundPos2) (posn-y foundPos2))