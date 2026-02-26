; Q4 Problem 3 — 6 balls, 1 gripper
; Expected: h_CG = 18, h* = 23, ratio ~= 0.783

(define (problem gripper1-p3)
  (:domain gripper-single)
  (:objects
    rooma roomb - room
    ball1 ball2 ball3 ball4 ball5 ball6 - ball)
  (:init
    (room rooma) (room roomb)
    (ball ball1) (ball ball2) (ball ball3)
    (ball ball4) (ball ball5) (ball ball6)
    (at-robby rooma)
    (at ball1 rooma) (at ball2 rooma) (at ball3 rooma)
    (at ball4 rooma) (at ball5 rooma) (at ball6 rooma)
    (free-gripper))
  (:goal (and (at ball1 roomb) (at ball2 roomb) (at ball3 roomb)
              (at ball4 roomb) (at ball5 roomb) (at ball6 roomb)))
)
