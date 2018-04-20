(define (domain robot-to-door)
		(:requirements :strips)
    (:predicates
			(at ?obj ?waypoint)
			(robot ?robot)
			(obstacle ?obstacle)
			(waypoint ?waypoint)
			(handempty)
			(moveable ?obj)
			(can-move ?from ?to)
			(clear ?waypoint)
    )

    (:action move
        :parameters
            (?robot
             ?from-waypoint
             ?to-waypoint)

        :precondition
            (and
                (robot ?robot)
                (waypoint ?from-waypoint)
                (waypoint ?to-waypoint)
                (at ?robot ?from-waypoint)
                (can-move ?from-waypoint ?to-waypoint)
								(clear ?to-waypoint)
								)

        :effect
            (and
                (at ?robot ?to-waypoint)
                (not (at ?robot ?from-waypoint)))
    ))
