import help_functions as hf
import copy

'''
State class which holds the state of the system
'''
class State:
	def __init__(self,domainclass=None,problem_file=None,parent_state=None,action=None,action_parameters=None):
		self.name 				= "" #name of the problem
		self.domain 			= "" #Name of the domain
		self.objects 			= [] #Objects in the current problem
		self.num_objects		= 0
		self.state 				= [] #State holds the predicates that defines the current state
		self.goal 				= [] #Goal state
		self.parent_action 		= action #name of the action
		self.depth 				= 0 #How many action in is the state
		self.cost 				= 0 #Estimated cost from initial state to goal state via this state
		self.domainclass 		= domainclass
		self.child_states 		= []
		self.action_parameters 	= action_parameters
		self.actions 			= []
		self.estimated_dist_to_goal = 0
		self.parent 			= parent_state

		if not parent_state:
			self.parse(problem_file)
			self.cost = self.ff_heuristic()

		else:
			self.actions 	= copy.copy(parent_state.actions)
			self.actions.append(action.name + ' ' + ' '.join(action_parameters))

			self.goal 		= parent_state.goal
			self.state 		= copy.copy(parent_state.state)
			self.depth 		= self.parent.depth + 1


			self.state.extend(action.get_addlist(action_parameters))
			self.objects 	= parent_state.objects

			delete_list 	= action.get_deletelist(action_parameters)
			for item in delete_list:
				self.state.remove(item.upper())

		self.state = sorted(self.state)

	def set_state_cost(self):
		self.cost = self.ff_heuristic() + self.depth

	def heuristic(self):
		dist_to_goal = 0
		#print 'p ness'
		# print len(self.state)
		for goals in self.goal:
			found_goal = False
			for state in self.state:
				#print goals==state
				if goals==state:
					found_goal = True
					break
			if not found_goal:
				dist_to_goal += 1
		# print dist_to_goal
		self.estimated_dist_to_goal = dist_to_goal
		return 1*dist_to_goal

	def ff_heuristic(self):
		state = self.state[:]
		cost = 0
		previous_lenght_state = len(state)
		while not self.is_goal_state_external(state):
			#Find possible actions
			add_list = []
			for action in self.domainclass.actions:
				return_parameters = action.return_possible(state)

				for parameters in return_parameters:
					new_items = action.get_addlist(parameters)
					add_list.extend(new_items)
			cost = cost + 1
			for add_state in add_list:
				if add_state not in state:
					state.append(add_state)
			#print cost,len(state)#,state
			if 	previous_lenght_state == len(state):
				a=1
				#raise ValueError('Error: Problem not solvable')
			previous_lenght_state = len(state)

			#print cost,len(state)
		self.estimated_dist_to_goal = cost + self.heuristic()
		return 10*(cost + self.heuristic())


	def create_child_states(self):
		for action in self.domainclass.actions:
			return_parameters = action.return_possible(self.state)
			for parameters in return_parameters:
				#if action.is_possible(self.state,parameters):
				self.child_states.append(State(domainclass=self.domainclass,parent_state=self,action = action,action_parameters=parameters))

	def get_child_states(self):
		return self.child_states

	def parse(self,problem_file):
		single_line=""
		for line in problem_file:
			line = line.strip()
			single_line = single_line + line + ' '
			single_line = single_line.upper()

			#single_line.strip()
		for element in hf.get_elements(single_line[1:-2]):
			element = hf.join(element)

			if element[0:6].lower() == "define":
				element = remove_white(element)
				self.name = element[7:-1]

			elif element[2:9].lower() == ":domain":
				element = remove_white(element)
				self.domain = element[8:-1].lower()

			elif element[2:10].lower()==":objects":
				self.set_objects(element)

			elif element[2:7].lower()==':init':
				element = element[6:-1]
				self.set_state(element)

			elif element[2:7].lower()==':goal':
				self.set_goal_state(element)
			else:
				print element[2:7]
				raise ValueError('Error in:',element,'Can not recognice this property. Problem File')

	def set_objects(self,objects):

		objects = objects[11:-1]

		letters = []
		for letter in objects:
			if letter == ' ':
				letter = ''

				if not letters==' ':
					self.objects.append(join(letters))
				letters=[]
			letters.append(letter)

		if not letters== ' ' and not letters:
			self.objects.append(join(letters))
		self.num_objects = len(self.objects)

	def set_state(self,state):
		states = hf.get_elements(state)
		for state in states:
			#states are seprated by space or new line so one need to distinguish
			i=0
			for letter in state:
				if letter=='(':
					self.state.append((join(state[i+1:-1])).upper())
					break
				i=i+1



		# print self.state

	def set_goal_state(self,goal):
		goal =  goal[7:]
		if remove_white(goal.lower()[2:6])=='and':
			goal = goal[6:]
		goals = hf.get_elements(goal[:-2])
		for goal in goals:
			i=0
			for letter in goal:
				if letter=='(':
					self.goal.append(join(goal[i+1:-1]))
					break
				i=i+1

	def is_goal_state(self):
		found_goal = False

		for goals in self.goal:
			found_goal = False
			for state in self.state:
				if goals==state:
					found_goal = True
					break
			if not found_goal:
				return False


		return True
				# print goal==state,goal,state

	def is_goal_state_external(self,state):
		found_goal = False

		for goals in self.goal:
			found_goal = False
			for states in state:
				if goals==states:
					found_goal = True
					break
			if not found_goal:
				return False
		return True

	def get_cost(self):
		return self.cost

	def __cmp__(self, other):
		#Used for heap sort
		return cmp(self.cost, other.cost)

def join(arr):
	#sets an array of chars to string
	return "".join(arr)

def remove_white(arr):
	arr = arr.replace(' ','')
	arr = arr.replace('	','')
	return arr

def items_in_list_are_unique(items):
	item_check_list = {}
	for item in items:
		if item in item_check_list:
			return False
		item_check_list[item]=True
	return True
