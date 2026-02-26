; Q2 Problem 1 — 1 door (trivial: no renewal needed)
; Expected: h^ff = 1, h* = 1, ratio = 1.00
; Optimal plan: use-key(d1)

(define (problem keydoors-p1)
  (:domain key-doors)
  (:objects d1 - door)
  (:init
    (key-ready)
    (door-closed d1))
  (:goal (door-open d1))
)
