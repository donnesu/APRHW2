; Q1 Problem 5 — 5 independent tasks
; Expected: h^ff = 5, h* = 5, ratio = 1.00

(define (problem tasks-p5)
  (:domain independent-tasks)
  (:objects t1 t2 t3 t4 t5 - task)
  (:init (pending t1) (pending t2) (pending t3) (pending t4) (pending t5))
  (:goal (and (completed t1) (completed t2) (completed t3)
              (completed t4) (completed t5)))
)
