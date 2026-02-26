; Q2: Key-Doors Domain
; The FF (relaxed plan) heuristic is INACCURATE on this domain.
;
; There is ONE shared key and n doors.  Opening any door consumes the key
; (removes key-ready, adds key-used).  The key must be renewed (reset)
; before the next door can be opened.
;
; FF ignores the delete effect "NOT key-ready", so in the relaxed plan it
; believes the key stays available and all n doors can be opened with n
; consecutive use-key actions.
;   h^ff = n
;
; In the real problem, after each use-key the key must be renewed before
; the next use:  use-key(d1), renew, use-key(d2), renew, ..., use-key(dn)
;   h*   = 2n - 1
;
; Ratio = n / (2n - 1)  decreasing toward 0.50 as n grows:
;   n=1: 1/1   = 1.00
;   n=2: 2/3  ~= 0.67
;   n=3: 3/5   = 0.60
;   n=4: 4/7  ~= 0.57
;   n=5: 5/9  ~= 0.56

(define (domain key-doors)
  (:requirements :strips :typing)
  (:types door)
  (:predicates
    (key-ready)           ; the shared key is available for use
    (key-used)            ; the key has been used and needs renewal
    (door-open  ?d - door)
    (door-closed ?d - door))

  ; Open a closed door using the key (consumes the key)
  (:action use-key
    :parameters (?d - door)
    :precondition (and (key-ready) (door-closed ?d))
    :effect (and (door-open ?d)
                 (not (door-closed ?d))
                 (key-used)
                 (not (key-ready))))

  ; Renew the key so it can be used again
  (:action renew-key
    :parameters ()
    :precondition (key-used)
    :effect (and (key-ready) (not (key-used))))
)
