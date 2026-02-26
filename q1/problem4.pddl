; Q1 Problem 4 — 4 independent tasks
; Expected: h^ff = 4, h* = 4, ratio = 1.00

(define (problem tasks-p4)
  (:domain independent-tasks)
  (:objects t1 t2 t3 t4 - task)
  (:init (pending t1) (pending t2) (pending t3) (pending t4))
  (:goal (and (completed t1) (completed t2) (completed t3) (completed t4)))
)
