(define (problem strips-sat-x-1)
(:domain satellite)
(:objects
	s0
	i0
	im1
	s2
	t0
	st0
	g1
	g2
	p3
	p4
	st5
	p6
)
(:init
	(satellite s0)
	(instrument i0)
	(supports i0 t0)
	(calibration_target i0 g2)
	(on_board i0 s0)
	(power_avail s0)
	(pointing s0 p6)
	(mode im1)
	(mode s2)
	(mode t0)
	(direction st0)
	(direction g1)
	(direction g2)
	(direction p3)
	(direction p4)
	(direction st5)
	(direction p6)
)
(:goal (and
	(have_image p4 t0)
	(have_image st5 t0)
	(have_image p6 t0)
))

)
