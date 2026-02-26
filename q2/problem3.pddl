; Q2 Problem 3 — 3 doors (2 renewals needed)
; Expected: h^ff = 3, h* = 5, ratio = 0.60
; Optimal plan: use-key(d1), renew, use-key(d2), renew, use-key(d3)

(define (problem keydoors-p3)
  (:domain key-doors)
  (:objects d1 d2 d3 - door)
  (:init
    (key-ready)
    (door-closed d1) (door-closed d2) (door-closed d3))
  (:goal (and (door-open d1) (door-open d2) (door-open d3)))
)
