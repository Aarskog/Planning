from parser import domain as dom
from parser import state as st

from heapq import heappush
from heapq import heappop
import time

class Solver:
	def __init__(self,domain_path,problem_path,print_progress=True,solver=None,weight=0.01):
		'''
		 Parse the given domain and problem file and try to solve it.
		'''

		'''
		Debug is used to see if the parser has read the files right
		'''
		debug = False


		'''
			profiling is used to see the time consumption of the solving process
		'''
		profiling = False


		domain_file = open(domain_path,'r')
		problem_file = open(problem_path,'r')

		try:
			'''Parse the files'''
			domain = dom.Domain(domain_file)
			init_state = st.State(domainclass = domain,problem_file=problem_file)

			start_time = time.time()

			if debug:
				self.debug(domain,init_state)

			if profiling:
				pr = cProfile.Profile()
				pr.enable()


			'''Solve the problem'''
			self.solution = self.solve(init_state,solver,print_progress,weight)


			if profiling:
				pr.disable()
				s = StringIO.StringIO()
				sortby = 'cumulative'
				ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
				ps.print_stats()
				print s.getvalue()

			if print_progress: print("--- %s seconds ---" % (time.time() - start_time))



		except ValueError as err:
			print '------------------'
			for arg in err.args:
				print arg
			print '------------------'

	def solve(self,initial_state,solver=None,print_progress=True,weight=0.01):

		heap = []

		heappush(heap,initial_state)
		visited_states = {tuple(initial_state.state):True}

		'''Variables for printing progress'''
		i = 0
		new_states_inserted = 0
		lowest_dist = float('inf')
		deepest = 0


		while heap:# and i < 1000 :

			#Get the state with the lowest cost from the heap
			possible_solution = heappop(heap)

			'''Updating variables for printing progress'''
			if possible_solution.estimated_dist_to_goal < lowest_dist and i:
				lowest_dist = possible_solution.estimated_dist_to_goal
			if possible_solution.depth > deepest and i:
				deepest = possible_solution.depth

			if print_progress:
				print 'Visited:',i,' len queue:',len(heap),' depth:',possible_solution.depth,deepest,\
			' New states:',new_states_inserted,' State cost: ',possible_solution.cost,\
			' Dist goal: ',possible_solution.estimated_dist_to_goal,lowest_dist#,len(possible_solution.state)



			if possible_solution.is_goal_state():
				if print_progress:
					print '\n\n----------Solution found!---------------\n'
					#print 'The state is:\n',possible_solution.state
					print '\n\nThe goal was:'
					for goal in possible_solution.goal: print goal
					print '\nLength of solution: ',len(possible_solution.actions)
					print '\nThe solution is: '
					for action in possible_solution.actions:
						print action
					print '\n\n'
				return possible_solution.actions


			else:
				possible_solution.create_child_states()
				new_states = possible_solution.get_child_states()
				new_states_inserted = 0
				for new_state in new_states:

					'''check if the state already has been visited using hash table'''
					if not tuple(new_state.state) in visited_states:
						new_state.set_state_cost(solver,weight)
						'''Add the new state to visited states'''
						visited_states[tuple(new_state.state)] = True
						new_states_inserted = new_states_inserted + 1

						'''Add the new state to the queue using a heap sorted based on
						the state cost'''
						heappush(heap,new_state)

			i = i + 1


		print '---NOT SOLVABLE---'
		print 'Nodes visited = ',i

	def debug(self,domain,init_state):
		print "\n\nDomain name: ",domain.domain_name
		for predicate in domain.predicates:
			print "Predicate: ",predicate.name,predicate.parameters

		for action in domain.actions:
			print "\n\nAction name:",action.name
			print "Parameters:", action.parameters
			for precondition in action.preconditions:
				print "Precondition: ",precondition.name,precondition.parameters

			for effect in action.effects:
				print "Effect: ",effect.name, effect.parameters
			for delete_effect in action.delete_effects:
				print "Delete effect: ",delete_effect.name,delete_effect.parameters


		print '\n----------Objects-----------------'
		for obj in init_state.objects:
			print obj
		print '\n-------INIT STATE-----------'
		for state in init_state.state:
			print state

		print '\n-------Goal-----------'
		for goal in init_state.goal:
			print goal

	def get_solution(self):
		return self.solution
