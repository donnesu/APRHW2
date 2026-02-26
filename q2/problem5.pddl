; Q2 Problem 5 — 5 doors (4 renewals needed)
; Expected: h^ff = 5, h* = 9, ratio ~= 0.56
; Optimal plan: use-key(d1), renew, use-key(d2), renew,
;               use-key(d3), renew, use-key(d4), renew, use-key(d5)

(define (problem keydoors-p5)
  (:domain key-doors)
  (:objects d1 d2 d3 d4 d5 - door)
  (:init
    (key-ready)
    (door-closed d1) (door-closed d2) (door-closed d3)
    (door-closed d4) (door-closed d5))
  (:goal (and (door-open d1) (door-open d2) (door-open d3)
              (door-open d4) (door-open d5)))
)
