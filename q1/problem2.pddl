; Q1 Problem 2 — 2 independent tasks
; Expected: h^ff = 2, h* = 2, ratio = 1.00

(define (problem tasks-p2)
  (:domain independent-tasks)
  (:objects t1 t2 - task)
  (:init (pending t1) (pending t2))
  (:goal (and (completed t1) (completed t2)))
)
