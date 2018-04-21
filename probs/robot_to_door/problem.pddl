(define (problem rtd)
(:domain robot-to-door)
(:objects
robot
door
waypoint0
waypoint1
waypoint2
waypoint3
waypoint4
waypoint5
waypoint6
waypoint7
obstacle1
obstacle2
obstacle3
obstacle4
obstacle5
obstacle6
)
(:init
(robot robot)
(door door)
(handempty)
(at robot waypoint0)
(waypoint waypoint0)
(clear waypoint0)
(waypoint waypoint1)
(waypoint waypoint2)
(waypoint waypoint3)
(waypoint waypoint4)
(waypoint waypoint5)
(waypoint waypoint6)
(waypoint waypoint7)
(clear waypoint7)
(can-move waypoint0 waypoint1)
(can-move waypoint0 waypoint2)
(can-move waypoint1 waypoint0)
(can-move waypoint1 waypoint3)
(can-move waypoint2 waypoint0)
(can-move waypoint2 waypoint3)
(can-move waypoint2 waypoint4)
(can-move waypoint3 waypoint1)
(can-move waypoint3 waypoint2)
(can-move waypoint3 waypoint5)
(can-move waypoint4 waypoint2)
(can-move waypoint4 waypoint5)
(can-move waypoint4 waypoint6)
(can-move waypoint5 waypoint3)
(can-move waypoint5 waypoint4)
(can-move waypoint5 waypoint7)
(can-move waypoint6 waypoint4)
(can-move waypoint6 waypoint7)
(can-move waypoint7 waypoint5)
(can-move waypoint7 waypoint6)
(obstacle obstacle1)
(moveable obstacle1)
(at obstacle1 waypoint4)
(obstacle obstacle2)
(moveable obstacle2)
(at obstacle2 waypoint5)
(obstacle obstacle3)
(moveable obstacle3)
(at obstacle3 waypoint3)
(obstacle obstacle4)
(moveable obstacle4)
(at obstacle4 waypoint2)
(obstacle obstacle5)
(moveable obstacle5)
(at obstacle5 waypoint1)
(obstacle obstacle6)
(moveable obstacle6)
(at obstacle6 waypoint6)
)
(:goal (and
(at robot waypoint7)
(handempty)
)))
