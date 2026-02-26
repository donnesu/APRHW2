; Q4 Problem 1 — 2 balls, 1 gripper
; Expected: h_CG = 6, h* = 7, ratio ~= 0.857
; Optimal plan: pick(b1,A), move(A,B), drop(b1,B), move(B,A),
;               pick(b2,A), move(A,B), drop(b2,B)

(define (problem gripper1-p1)
  (:domain gripper-single)
  (:objects
    rooma roomb - room
    ball1 ball2 - ball)
  (:init
    (room rooma) (room roomb)
    (ball ball1) (ball ball2)
    (at-robby rooma)
    (at ball1 rooma) (at ball2 rooma)
    (free-gripper))
  (:goal (and (at ball1 roomb) (at ball2 roomb)))
)
