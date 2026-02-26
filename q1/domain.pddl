; Q1: Independent Tasks Domain
; The FF (relaxed plan) heuristic is ACCURATE on this domain.
;
; Each task can be completed with exactly one action and there are no
; interactions between tasks (no shared preconditions or negative effects
; that interfere with other tasks). Therefore the relaxed plan equals the
; real optimal plan: h^ff = h* = n tasks, giving ratio = 1.0 for all sizes.

(define (domain independent-tasks)
  (:requirements :strips :typing)
  (:types task)
  (:predicates
    (pending ?t - task)
    (completed ?t - task))

  (:action do-task
    :parameters (?t - task)
    :precondition (pending ?t)
    :effect (and (completed ?t) (not (pending ?t))))
)
