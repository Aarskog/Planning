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
			self.cost = self.heuristic()

		else:
			self.actions 	= copy.copy(parent_state.actions)
			self.actions.append(action.name + ' ' + ' '.join(action_parameters))

			self.goal 		= parent_state.goal
			self.state 		= copy.copy(parent_state.state)
			self.depth 		= self.parent.depth + 1
			self.cost 		= self.heuristic() + self.depth
			self.state.extend(action.get_addlist(action_parameters))
			self.objects 	= parent_state.objects


			delete_list 	= action.get_deletelist(action_parameters)
			for item in delete_list:
				self.state.remove(item.upper())

		self.state = sorted(self.state)

	def heuristic(self):
		dist_to_goal = 0
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
		return 20*dist_to_goal

	def create_child_states2(self):
		for action in self.domainclass.actions:
			return_parameters = action.return_possible(self.state)
			for parameters in return_parameters:
				if action.is_possible(self.state,parameters):
					print 'gogo'
					self.child_states.append(State(domainclass=self.domainclass,parent_state=self,action = action,action_parameters=parameters))
				#else:
					#print 'action no go'

	def create_child_states(self):
		# print '-------------start-------------------------------------'
		for action in self.domainclass.actions:

			self.recursion_set_states(action,action.num_parameters,self.objects,[])
		# print '----------------------end----------------------------'

	def recursion_set_states(self,action,num_parameters,objects,current_objects):
		#current_objects = copy.deepcopy(current_objects)
		if num_parameters > 1:
			for objct in objects:
				current_objects_copy = copy.deepcopy(current_objects)
				current_objects_copy.append(objct)
				self.recursion_set_states(action,num_parameters-1,objects,current_objects_copy)

		else:

			for objct in objects:
				current_objects_copy = copy.deepcopy(current_objects)
				current_objects_copy.append(objct)
				# print current_objects_copy
				if items_in_list_are_unique(current_objects_copy):
					if action.is_possible(self.state,current_objects_copy):
						#print current_objects_copy
						# print 'npw-----------------------------------------'
						self.child_states.append(State(domainclass=self.domainclass,parent_state=self,action = action,action_parameters=current_objects_copy))
						# print action.name + ' ' + ' '.join(current_objects_copy)

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
