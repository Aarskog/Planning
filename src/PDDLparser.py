import domain as dom
import state as st
import os
from heapq import heappush
from heapq import heappop

def a_star_solve(initial_state):
	heap = []

	heappush(heap,initial_state)
	visited_states = {tuple(initial_state.state):True}

	i = 0

	while heap:

		#Get the state with the lowest cost from the heap
		possible_solution = heappop(heap)

		if possible_solution.is_goal_state():
			print 'Success!!'
			print possible_solution.state
			print 'Length of solution: ',len(possible_solution.actions)

			for action in possible_solution.actions:
				print action
			return

		else:
			possible_solution.create_child_states()
			new_states = possible_solution.get_child_states()
			new_states_inserted = 0
			for new_state in new_states:

				#check if the state already has been visited using hash table
				if not tuple(new_state.state) in visited_states:

					#Add the new state to visited states
					visited_states[tuple(new_state.state)] = True
					new_states_inserted = new_states_inserted +1

					#Add the new state to the queue using a heap sorted based on
					#the state cost
					heappush(heap,new_state)

		i = i + 1
		print 'states visited:',i,' length queue:',len(heap),' depth:',possible_solution.depth,\
		' New states:',new_states_inserted,' State cost: ',possible_solution.cost,\
		' Dist to goal: ',possible_solution.estimated_dist_to_goal

	print '---NOT SOLVABLE---'
	print 'Nodes visited = ',i
	print q

def main():

	dir_path = os.path.dirname(os.path.realpath(__file__))
	dir_path = dir_path[:-3]

	debug = False
	# debug = True



	domain_file_name = dir_path+'probs/satellite/domain.pddl'
	problem_file_name = dir_path+'probs/satellite/problem01.pddl'
    # #
	problem_file_name = dir_path+'probs/blocks/problem.pddl'
	domain_file_name = dir_path+'probs/blocks/domain.pddl'

	# problem_file_name = dir_path+'probs/aircargo/problem.pddl'
	# domain_file_name = dir_path+'probs/aircargo/domain.pddl'
	#

	domain_file = open(domain_file_name,'r')
	problem_file = open(problem_file_name,'r')

	try:
		domain = dom.Domain(domain_file)
		init_state = st.State(domainclass = domain,problem_file=problem_file)

		a_star_solve(init_state)

		if debug:
			print "\n\nDomain name: ",domain.domain_name
			for predicate in domain.predicates:
				print "\n------------------------------"
				print "Predicate name: ",predicate.name
				print "Predicate params: ",predicate.parameters
				print "------------------------------\n"

			for action in domain.actions:
				print "\n\n------Action name: ",action.name,"-------------"
				print "Parameters:", action.parameters
				for precondition in action.preconditions:
					print "------------------------------"
					print "Precondition name: ",precondition.name
					print "Precondition param: ",precondition.parameters
					print "------------------------------\n"
				for effect in action.effects:
					print "------------------------------"
					print "Effect name: ",effect.name
					print "Effect params: ", effect.parameters
					print "------------------------------\n"
				for delete_effect in action.delete_effects:
					print "------------------------------"
					print "Delete effect name: ",delete_effect.name
					print "Delete effect params: ", delete_effect.parameters
					print "------------------------------\n"

	except ValueError as err:
		print '------------------'
		for arg in err.args:
			print arg
		print '------------------'

	domain_file.close()
	problem_file.close()

if __name__=='__main__':
	main()


#Fix naar action bare har en effect. Det blir rart
