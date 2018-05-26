import os

from solver import solver as sv
from problems import domain_rob_to_door as drtd

def main():

	'''
		Get the current directory
	'''
	dir_path = os.path.dirname(os.path.realpath(__file__))
	dir_path = dir_path[:-3]




	'''
		Switch between solving methods: BFS,DFS, Weitgthed A* with missing subgoals heuristic
		or relaxed problem heuristic

		The weighted A* is made as f(s) = h(s) + w*g(s), such that if w = 0 it is
		best first search
	'''
	# solver = 'bfs'
	# solver = 'dfs'
	# solver = 'relaxed'
	solver = 'missing state'
	weight = 0.01


	'''
	Choose whether to solve the robot_to_door replanning problem or choose a problem
	from the ICAPS competition
	'''
	rob2door = False
	# rob2door = True

	if rob2door:
		'''
			Robot to door is a special made scenario where the robot must
			replan in order to reach its goal. The problem.pddl is automatically
			generated based on the inputs seen below.
		'''
		path = dir_path+'probs/robot_to_door/problem.pddl'

		world_size = (4,5)
		rob_pos = (0,0)
		door_pos = (world_size[0]-1,world_size[1]-1)
		obstacles = [drtd.Obstacle((2,0)),drtd.Obstacle((1,0)),drtd.Obstacle((3,0)),\
		drtd.Obstacle_hidden((0,1),False),drtd.Obstacle_hidden((1,1),False),drtd.Obstacle_hidden((2,1),False),drtd.Obstacle((3,1)),\
		drtd.Obstacle((0,2)),drtd.Obstacle((1,2)),drtd.Obstacle((2,2)),drtd.Obstacle((3,2)),
		drtd.Obstacle((0,3)),drtd.Obstacle_hidden((1,3),False),drtd.Obstacle_hidden((2,3),False),drtd.Obstacle_hidden((3,3),False)]

		dom24 = drtd.Domain_rob_to_door(world_size,rob_pos,door_pos,path=path,obstacles=obstacles)

		problem_file_name = dir_path+'probs/robot_to_door/problem.pddl'
		domain_file_name = dir_path+'probs/robot_to_door/domain.pddl'
	else:

		'''
		Different PDDL scenarios. Comment/uncomment to use
		'''


		# Satellite problem.
		domain_file_name = dir_path+'probs/satellite/domain.pddl'
		problem_file_name = dir_path+'probs/satellite/problem01.pddl'

		#Block world
		# problem_file_name = dir_path+'probs/blocks/problem.pddl'
		# domain_file_name = dir_path+'probs/blocks/domain.pddl'

		# Aircargo problem
		# problem_file_name = dir_path+'probs/aircargo/problem.pddl'
		# domain_file_name = dir_path+'probs/aircargo/domain.pddl'


		# Shakey
		# problem_file_name = dir_path+'probs/shakey/problem1.pddl'
		# domain_file_name = dir_path+'probs/shakey/domain.pddl'


		# Rover1
		# problem_file_name = dir_path+'probs/rover/problem.pddl'
		# domain_file_name = dir_path+'probs/rover/domain.pddl'


		# Rover2
		# problem_file_name = dir_path+'probs/rover2/problem.pddl'
		# domain_file_name = dir_path+'probs/rover2/domain.pddl'


 	solv = sv.Solver(domain_file_name,problem_file_name,solver=solver,weight=weight)
	solution = solv.get_solution()



	#Execute plan for robot to door
	if rob2door:
		print '\nInitial state'
		dom24.print_room()
		print '\n'

		i = 0
		while solution:
			action = solution.pop(0)
			print '\n'

			if not dom24.do_action(action):

				print 'Can not pick up. Replanning...'
				solv = sv.Solver(domain_file_name,problem_file_name,print_progress=False)
				solution = solv.get_solution()
				print 'Replanning done'
				#i = i - 1
			i = i + 1
		print i,' actions attempted'


if __name__=='__main__':
	main()
