; Q4 Problem 2 — 4 balls, 1 gripper
; Expected: h_CG = 12, h* = 15, ratio = 0.800

(define (problem gripper1-p2)
  (:domain gripper-single)
  (:objects
    rooma roomb - room
    ball1 ball2 ball3 ball4 - ball)
  (:init
    (room rooma) (room roomb)
    (ball ball1) (ball ball2) (ball ball3) (ball ball4)
    (at-robby rooma)
    (at ball1 rooma) (at ball2 rooma) (at ball3 rooma) (at ball4 rooma)
    (free-gripper))
  (:goal (and (at ball1 roomb) (at ball2 roomb)
              (at ball3 roomb) (at ball4 roomb)))
)
