import domain as dom
import state as st
import os


def a_star_solve(initial_state):
	q = [initial_state]
	visited_states = {tuple(initial_state.state):True}

	# print initial_state.is_goal_state()

	i = 0

	while q:
		possible_solution = q.pop()
		#print  possible_solution.is_goal_state()
		if possible_solution.is_goal_state():
			print 'Success!!'
			print possible_solution.state
			return

		else:
			possible_solution.create_child_states()
			new_states = possible_solution.get_child_states()

			for new_state in new_states:
				# print '______--__________'
				# print new_state.state
				# print tuple(new_state.state) in visited_states
				# print '___________________'

				if not tuple(new_state.state) in visited_states:
					visited_states[tuple(new_state.state)] = True

					inserted = False

					# for k in range(0,len(q)):
					# 	if new_state.get_cost() <= q[k].get_cost():
					# 		q.insert(k,new_state)
					# 		inserted = True
					# 		break
					if not inserted:
						q.insert(len(q),new_state)
			# print 'lenq',len(q)
		i = i + 1
		print i,'states visited',len(q),possible_solution.get_cost()

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
    #
	problem_file_name = dir_path+'probs/blocks/problem.pddl'
	domain_file_name = dir_path+'probs/blocks/domain.pddl'

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
