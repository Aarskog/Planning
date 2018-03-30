
(define (domain shakey)
  (:requirements :strips)

  (:predicates
    (is-room ?room)
    (is-lit ?room)
		(is-dark ?room)

    (is-tiny-door ?door)
    (is-wide-door ?door)
    (are-linked-by ?room-a ?room-b ?door)

    (is-shakey ?shak)

    (is-gripper ?grip)
    (is-gripper-empty ?grip)

    (is-tablet ?tablet)

    (is-small-obj ?obj)
    (is-on-floor ?obj)
    (is-in-grip ?obj ?grip)
    (is-on-tablet ?obj)

    (is-box ?big-box)

    (is-in ?any-objects ?room)



		)

  (:action shakey_changes_room
    :parameters (?shak ?room-a ?room-b ?door)
    :precondition (and
      (is-shakey ?shak)(is-in ?shak ?room-a)
      (is-room ?room-a)(is-room ?room-b)
      (are-linked-by ?room-a ?room-b ?door)
    )
    :effect (and
      (is-in ?shak ?room-b)
      (not (is-in ?shak ?room-a) )
    )
  )

  (:action shakey_pushes_box
    :parameters (?shak ?box ?room-a ?room-b ?wide-door)
    :precondition (and
      (is-shakey ?shak)(is-in ?shak ?room-a)
      (is-box ?box)(is-in ?box ?room-a)
      (is-room ?room-a)(is-room ?room-b)
      (is-wide-door ?wide-door)
      (are-linked-by ?room-a ?room-b ?wide-door)
    )
    :effect (and
      (is-in ?box ?room-b)
      (not (is-in ?box ?room-a) )
    )
  )

  (:action shakey_turns_lights_on
    :parameters (?shak ?box ?room)
    :precondition (and
      (is-shakey ?shak)(is-in ?shak ?room)
      (is-box ?box)(is-in ?box ?room)
      (is-room ?room)
			(is-dark ?room)
      )
    :effect (and (is-lit ?room) (not (is-dark ?room))))

  (:action shakey_turns_lights_off
    :parameters (?shak ?box ?room)
    :precondition (and
      (is-shakey ?shak)(is-in ?shak ?room)
      (is-box ?box)(is-in ?box ?room)
      (is-room ?room)
      (is-lit ?room))
    :effect (and (not (is-lit ?room))
		(is-dark ?room)))

  (:action shakey_picks_small_obj_in_gripper
    :parameters (?shak ?grip ?obj ?room)
    :precondition (and
      (is-shakey ?shak)(is-in ?shak ?room)
      (is-gripper ?grip) (is-gripper-empty ?grip)
      (is-small-obj ?obj)(is-in ?obj ?room)(is-on-floor ?obj)
      (is-room ?room)(is-lit ?room))

    ;; Note that both "is-in" is used in pair
    ;; with the other more precise "in" operators.
    :effect (and
      (not (is-gripper-empty ?grip) )
      (not (is-in ?obj ?room))
      (not (is-on-floor ?obj) )
      (is-in ?obj ?grip)
      (is-in-grip ?obj ?grip)
    )
  )

  (:action shakey_places_small_obj_on_tablet
    :parameters (?shak ?grip ?obj ?tablet ?room)
    :precondition (and
      (is-shakey ?shak)(is-in ?shak ?room)
      (is-gripper ?grip)
      (is-small-obj ?obj)(is-in ?obj ?grip)(is-in-grip ?obj ?grip)
      (is-tablet ?tablet) (is-in ?tablet ?room)
      (is-room ?room)(is-lit ?room))


    :effect (and
      (not (is-in ?obj ?grip) )
      (not (is-in-grip ?obj ?grip))
      (is-in ?obj ?room)
      (is-in ?obj ?tablet)
      (is-gripper-empty ?grip)
      (is-on-tablet ?obj)
    )
  )

)
