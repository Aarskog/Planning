(define (problem shakey-task-2-3rooms-4objs)
(:domain shakey)
(:objects
  room00 room10 room20
  tiny-door-00-10 tiny-door-10-20
  wide-door-00-10 wide-door-10-20
  tablet
  shak
  grip1 grip2
  obj0 obj1 obj2 obj3
  box
)
(:init
  ;; static:
  (is-room room00) (is-room room10) (is-room room20)
  (is-tiny-door tiny-door-00-10) (are-linked-by room00 room10 tiny-door-00-10) (are-linked-by room10 room00 tiny-door-00-10)
  (is-tiny-door tiny-door-10-20) (are-linked-by room10 room20 tiny-door-10-20) (are-linked-by room20 room10 tiny-door-10-20)
  (is-wide-door wide-door-00-10) (are-linked-by room00 room10 wide-door-00-10) (are-linked-by room10 room00 wide-door-00-10)
  (is-wide-door wide-door-10-20) (are-linked-by room10 room20 wide-door-10-20) (are-linked-by room20 room10 wide-door-10-20)
  (is-tablet tablet) (is-in tablet room00)
  ;; dynamic:
  (is-shakey shak) (is-in shak room00)
  (is-gripper grip1) (is-gripper-empty grip1)
  (is-gripper grip2) (is-gripper-empty grip2)
  (is-small-obj obj0) (is-on-floor obj0) (is-in obj0 room00)
  (is-small-obj obj1) (is-on-floor obj1) (is-in obj1 room10)
  (is-small-obj obj2) (is-on-floor obj2) (is-in obj2 room20)
  (is-small-obj obj3) (is-on-floor obj3) (is-in obj3 room00)
  (is-box box) (is-in box room00)
	(is-dark room00)
	(is-dark room10)
	(is-dark room20))
(:goal (and (is-in shak room00)
    (is-gripper-empty grip1)
    (is-gripper-empty grip2)
    (is-on-tablet obj0)
    (is-on-tablet obj1)
    (is-on-tablet obj2)
    (is-on-tablet obj3)
    (is-dark room00)
    (is-dark room10)
    (is-dark room20)
    (is-in box room00))))
