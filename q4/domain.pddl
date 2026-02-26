; Q4: Single-Gripper Domain (Extra Credit)
; The Causal Graph (CG) heuristic is INACCURATE on this domain.
;
; A robot with ONE gripper moves n balls from room A to room B, one ball
; at a time.  Each round trip requires:
;   pick(ball, A), move(A->B), drop(ball, B), move(B->A)  [4 steps]
; except the last trip which needs no return:
;   pick(ball, A), move(A->B), drop(ball, B)  [3 steps]
; Optimal cost:  h* = 4n - 1
;
; The CG heuristic decomposes the problem ball-by-ball using the Domain
; Transition Graph (DTG) of each ball's location variable.  It estimates
; the per-ball cost as 3 (pick + move + drop) and sums these up, treating
; the single move A->B as shared across all balls.  CG misses the return
; trip the robot must make between deliveries.
;   h_CG = 3n
;
; Ratio = 3n / (4n - 1)  decreases toward 0.75 as n grows:
;   n= 2:  6/ 7 ~= 0.857
;   n= 4: 12/15  = 0.800
;   n= 6: 18/23 ~= 0.783
;   n= 8: 24/31 ~= 0.774
;   n=10: 30/39 ~= 0.769

(define (domain gripper-single)
  (:requirements :strips :typing)
  (:types room ball)
  (:predicates
    (room         ?r - room)
    (ball         ?b - ball)
    (at-robby     ?r - room)
    (at           ?b - ball ?r - room)
    (free-gripper)
    (carry        ?b - ball))

  (:action move
    :parameters (?from ?to - room)
    :precondition (and (room ?from) (room ?to) (at-robby ?from))
    :effect (and (at-robby ?to) (not (at-robby ?from))))

  (:action pick
    :parameters (?obj - ball ?room - room)
    :precondition (and (ball ?obj) (room ?room)
                       (at ?obj ?room) (at-robby ?room) (free-gripper))
    :effect (and (carry ?obj)
                 (not (at ?obj ?room))
                 (not (free-gripper))))

  (:action drop
    :parameters (?obj - ball ?room - room)
    :precondition (and (ball ?obj) (room ?room)
                       (carry ?obj) (at-robby ?room))
    :effect (and (at ?obj ?room)
                 (free-gripper)
                 (not (carry ?obj))))
)
