import domain as dom
import state as st
import os
from heapq import heappush
from heapq import heappop
import time
from graph_tool.all import *
import matplotlib
import networkx as nx
import matplotlib.pyplot as plt

import numpy as np
import cProfile, pstats, StringIO

def a_star_solve(initial_state,domain):

	initial_state.set_vertex()

	heap = []

	heappush(heap,initial_state)
	visited_states = {tuple(initial_state.state):True}

	i = 0
	new_states_inserted = 0
	lowest_dist = float('inf')
	deepest = 0
	while heap:# and i < 1000 :

		#Get the state with the lowest cost from the heap
		possible_solution = heappop(heap)

		# possible_solution_v = g.add_vertex()



		if possible_solution.estimated_dist_to_goal < lowest_dist:
			lowest_dist = possible_solution.estimated_dist_to_goal
		if possible_solution.depth > deepest:
			deepest = possible_solution.depth

		print 'Visited:',i,' len queue:',len(heap),' depth:',possible_solution.depth,deepest,\
		' New states:',new_states_inserted,' State cost: ',possible_solution.cost,\
		' Dist goal: ',possible_solution.estimated_dist_to_goal,lowest_dist#,len(possible_solution.state)

		if possible_solution.is_goal_state():
			print '\n\n----------Solution found!---------------\n'
			print 'The state is:\n'
			for st in possible_solution.state: print st
			print '\n\nThe goal was:'
			for goal in possible_solution.goal: print goal
			print '\nLength of solution: ',len(possible_solution.actions)
			print '\nThe solution is: '
			for action in possible_solution.actions:
				print action
			print_graph(domain.graph,possible_solution)
			#nx.draw_graphviz(domain.Graph)
			#plt.show()



			return


		else:
			possible_solution.create_child_states()
			new_states = possible_solution.get_child_states()
			new_states_inserted = 0
			for new_state in new_states:

				#check if the state already has been visited using hash table
				if not tuple(new_state.state) in visited_states:

					# new_state_v = g.add_vertex()
					new_state.set_vertex()
					new_state.set_edge(possible_solution.vertex)

					new_state.set_state_cost()
					#Add the new state to visited states
					visited_states[tuple(new_state.state)] = True
					new_states_inserted = new_states_inserted + 1

					#Add the new state to the queue using a heap sorted based on
					#the state cost
					heappush(heap,new_state)



		i = i + 1


	print '---NOT SOLVABLE---'
	print 'Nodes visited = ',i

def highlight_solution(state,ecolor,ewidth):
	if state.parent:
		ecolor[state.edge] = '#a40000'
		ewidth[state.edge] = 1
		highlight_solution(state.parent,ecolor,ewidth)

def print_graph(g,goal_state):
	vlist = shortest_distance(g, source=g.vertex(0),target=goal_state.vertex)
	#graph_tool.topology.mark_subgraph(g, sub,1)


	touch_v = g.new_vertex_property("bool")
	touch_e = g.new_edge_property("bool")
	ecolor = g.new_edge_property("string")
	ewidth = g.new_edge_property("double")
	ewidth.a = 0.4

	for e in g.edges():
		ecolor[e] = "#3465a4"

	highlight_solution(goal_state,ecolor,ewidth)

	pos = fruchterman_reingold_layout(g, n_iter=1000)#GOOD
	graph_draw(g, vertex_fill_color="#000000",pos=pos, \
               #vcmap=matplotlib.cm.binary, \
               edge_pen_width=ewidth, edge_color=ecolor,vertex_size=3,\
			    output="asta.pdf")

	#graph_draw(g, vertex_text=g.vertex_index,output_size=(2000, 2000), output="two-nodes.pdf")


def main():

	dir_path = os.path.dirname(os.path.realpath(__file__))
	dir_path = dir_path[:-3]

	debug = False
	# debug = True



	# satellite problem. shortest solution = 9
	# domain_file_name = dir_path+'probs/satellite/domain.pddl'
	# problem_file_name = dir_path+'probs/satellite/problem01.pddl'
	# # #
	# #
	# # #Block world
	# problem_file_name = dir_path+'probs/blocks/problem.pddl'
	# domain_file_name = dir_path+'probs/blocks/domain.pddl'


	# # # #aircargo problem shortest solution = 6
	problem_file_name = dir_path+'probs/aircargo/problem.pddl'
	domain_file_name = dir_path+'probs/aircargo/domain.pddl'


	# # # # Shakey shortest solution = 22      HSP A* = 26
	# problem_file_name = dir_path+'probs/shakey/problem1.pddl'
	# domain_file_name = dir_path+'probs/shakey/domain.pddl'
	# #

 	# # # # # # #Rover1 # shortest solution = 53
	# problem_file_name = dir_path+'probs/rover/problem.pddl'
	# domain_file_name = dir_path+'probs/rover/domain.pddl'


 	# # # # # #Rover2 shortest solution = 10
	# problem_file_name = dir_path+'probs/rover2/problem.pddl'
	# domain_file_name = dir_path+'probs/rover2/domain.pddl'




	domain_file = open(domain_file_name,'r')
	problem_file = open(problem_file_name,'r')

	try:
		g = Graph()
		domain = dom.Domain(domain_file,g)
		init_state = st.State(domainclass = domain,problem_file=problem_file)

		start_time = time.time()

		profiling = False
		# profiling = True
		if profiling:
			pr = cProfile.Profile()
			pr.enable()

		if debug:
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

		a_star_solve(init_state,domain)

		if profiling:
			pr.disable()
			s = StringIO.StringIO()
			sortby = 'cumulative'
			ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
			ps.print_stats()
			print s.getvalue()



		print("--- %s seconds ---" % (time.time() - start_time))



	except ValueError as err:
		print '------------------'
		for arg in err.args:
			print arg
		print '------------------'

	domain_file.close()
	problem_file.close()

if __name__=='__main__':
	main()

#https://github.com/primaryobjects/strips/tree/master/strips
#Fix naar action bare har en effect. Det blir rart
