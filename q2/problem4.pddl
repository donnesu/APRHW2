; Q2 Problem 4 — 4 doors (3 renewals needed)
; Expected: h^ff = 4, h* = 7, ratio ~= 0.57
; Optimal plan: use-key(d1), renew, use-key(d2), renew,
;               use-key(d3), renew, use-key(d4)

(define (problem keydoors-p4)
  (:domain key-doors)
  (:objects d1 d2 d3 d4 - door)
  (:init
    (key-ready)
    (door-closed d1) (door-closed d2) (door-closed d3) (door-closed d4))
  (:goal (and (door-open d1) (door-open d2) (door-open d3) (door-open d4)))
)
