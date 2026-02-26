; Q1 Problem 1 — 1 independent task
; Expected: h^ff = 1, h* = 1, ratio = 1.00

(define (problem tasks-p1)
  (:domain independent-tasks)
  (:objects t1 - task)
  (:init (pending t1))
  (:goal (completed t1))
)
