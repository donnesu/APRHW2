; Q1 Problem 3 — 3 independent tasks
; Expected: h^ff = 3, h* = 3, ratio = 1.00

(define (problem tasks-p3)
  (:domain independent-tasks)
  (:objects t1 t2 t3 - task)
  (:init (pending t1) (pending t2) (pending t3))
  (:goal (and (completed t1) (completed t2) (completed t3)))
)
