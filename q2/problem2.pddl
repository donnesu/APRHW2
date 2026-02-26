; Q2 Problem 2 — 2 doors (1 renewal needed)
; Expected: h^ff = 2, h* = 3, ratio ~= 0.67
; Optimal plan: use-key(d1), renew-key, use-key(d2)

(define (problem keydoors-p2)
  (:domain key-doors)
  (:objects d1 d2 - door)
  (:init
    (key-ready)
    (door-closed d1) (door-closed d2))
  (:goal (and (door-open d1) (door-open d2)))
)
