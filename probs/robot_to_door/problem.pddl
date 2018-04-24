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
waypoint8
waypoint9
waypoint10
waypoint11
waypoint12
waypoint13
waypoint14
waypoint15
waypoint16
waypoint17
waypoint18
waypoint19
obstacle1
obstacle2
obstacle3
obstacle4
obstacle5
obstacle6
obstacle7
obstacle8
obstacle9
obstacle10
obstacle11
obstacle12
obstacle13
obstacle14
obstacle15
)
(:init
(robot robot)
(door door)
(handempty)
(at robot waypoint7)
(waypoint waypoint0)
(waypoint waypoint1)
(waypoint waypoint2)
(waypoint waypoint3)
(waypoint waypoint4)
(clear waypoint4)
(waypoint waypoint5)
(waypoint waypoint6)
(waypoint waypoint7)
(clear waypoint7)
(waypoint waypoint8)
(waypoint waypoint9)
(clear waypoint9)
(waypoint waypoint10)
(waypoint waypoint11)
(waypoint waypoint12)
(waypoint waypoint13)
(waypoint waypoint14)
(clear waypoint14)
(waypoint waypoint15)
(waypoint waypoint16)
(waypoint waypoint17)
(waypoint waypoint18)
(waypoint waypoint19)
(clear waypoint19)
(can-move waypoint0 waypoint1)
(can-move waypoint0 waypoint5)
(can-move waypoint1 waypoint0)
(can-move waypoint1 waypoint2)
(can-move waypoint1 waypoint6)
(can-move waypoint2 waypoint1)
(can-move waypoint2 waypoint3)
(can-move waypoint2 waypoint7)
(can-move waypoint3 waypoint2)
(can-move waypoint3 waypoint4)
(can-move waypoint3 waypoint8)
(can-move waypoint4 waypoint3)
(can-move waypoint4 waypoint9)
(can-move waypoint5 waypoint0)
(can-move waypoint5 waypoint6)
(can-move waypoint5 waypoint10)
(can-move waypoint6 waypoint1)
(can-move waypoint6 waypoint5)
(can-move waypoint6 waypoint7)
(can-move waypoint6 waypoint11)
(can-move waypoint7 waypoint2)
(can-move waypoint7 waypoint6)
(can-move waypoint7 waypoint8)
(can-move waypoint7 waypoint12)
(can-move waypoint8 waypoint3)
(can-move waypoint8 waypoint7)
(can-move waypoint8 waypoint9)
(can-move waypoint8 waypoint13)
(can-move waypoint9 waypoint4)
(can-move waypoint9 waypoint8)
(can-move waypoint9 waypoint14)
(can-move waypoint10 waypoint5)
(can-move waypoint10 waypoint11)
(can-move waypoint10 waypoint15)
(can-move waypoint11 waypoint6)
(can-move waypoint11 waypoint10)
(can-move waypoint11 waypoint12)
(can-move waypoint11 waypoint16)
(can-move waypoint12 waypoint7)
(can-move waypoint12 waypoint11)
(can-move waypoint12 waypoint13)
(can-move waypoint12 waypoint17)
(can-move waypoint13 waypoint8)
(can-move waypoint13 waypoint12)
(can-move waypoint13 waypoint14)
(can-move waypoint13 waypoint18)
(can-move waypoint14 waypoint9)
(can-move waypoint14 waypoint13)
(can-move waypoint14 waypoint19)
(can-move waypoint15 waypoint10)
(can-move waypoint15 waypoint16)
(can-move waypoint16 waypoint11)
(can-move waypoint16 waypoint15)
(can-move waypoint16 waypoint17)
(can-move waypoint17 waypoint12)
(can-move waypoint17 waypoint16)
(can-move waypoint17 waypoint18)
(can-move waypoint18 waypoint13)
(can-move waypoint18 waypoint17)
(can-move waypoint18 waypoint19)
(can-move waypoint19 waypoint14)
(can-move waypoint19 waypoint18)
(obstacle obstacle1)
(moveable obstacle1)
(at obstacle1 waypoint5)
(obstacle obstacle2)
(moveable obstacle2)
(at obstacle2 waypoint0)
(obstacle obstacle3)
(moveable obstacle3)
(at obstacle3 waypoint10)
(obstacle obstacle4)
(at obstacle4 waypoint1)
(obstacle obstacle5)
(at obstacle5 waypoint6)
(obstacle obstacle6)
(at obstacle6 waypoint11)
(obstacle obstacle7)
(moveable obstacle7)
(at obstacle7 waypoint15)
(obstacle obstacle8)
(moveable obstacle8)
(at obstacle8 waypoint2)
(obstacle obstacle9)
(moveable obstacle9)
(at obstacle9 waypoint12)
(obstacle obstacle10)
(moveable obstacle10)
(at obstacle10 waypoint17)
(obstacle obstacle11)
(moveable obstacle11)
(at obstacle11 waypoint16)
(obstacle obstacle12)
(moveable obstacle12)
(at obstacle12 waypoint3)
(obstacle obstacle13)
(at obstacle13 waypoint8)
(obstacle obstacle14)
(at obstacle14 waypoint13)
(obstacle obstacle15)
(at obstacle15 waypoint18)
)
(:goal (and
(at robot waypoint19)
(handempty)
)))
