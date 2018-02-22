import copy



class Action:
	action_name = ''
	parameters = []
	preconditions = []
	effects = []
	def __init__(self,action):

		print '----------------------------'
		elements = get_elements(action)

		for element in elements:
			element =  "".join(element)
			#print element
			
			if element[0]!=':':
				self.set_name_and_parameters(element)
			elif element[0:13] == ':precondition':
				self.set_preconditions(element)

			else:
				#print element
				a=1



	def set_name_and_parameters(self,name_and_params):
		#print name_and_params
		letters = []
		i = 0

		for letter in name_and_params:

			if letter ==':':
				self.name="".join(letters)
				letters = []

			letters.append(letter)
			i = i + 1
	def set_preconditions(self,preconditions):
		element= preconditions[14:-1]
		#print element

		#ignore 'and' statement since strips only allows conjunctions
		if element[0:3]=='and':
			element=element[3:]
		#print element

		if element[0]=='(':
			preconditions = get_elements(element)
			#print preconditions
			for precondition in preconditions:
				precondition =  "".join(precondition)[1:-1]
				self.preconditions.append(Predicate(precondition))
		else:
			self.preconditions.append(Predicate(element))

class Predicate:
	name = ''
	parameters = []
	
	def __init__(self,predicate):
		#print "".join(predicate)
		self.parameters=[]
		letters = []
		named = False

		i = 0
		#print predicate
		for letter in predicate:
			if letter=='?':
				if not self.name:
					self.name = ''.join(letters)
					letters=[]
					named = True

				self.parameters.append(predicate[i + 1])

			letters.append(letter)
			i = i + 1

		if not named:
			self.name = ''.join(predicate)

	

class Domain:
	domain_name = ''
	requirements = []
	predicates = []
	actions = []
	def __init__(self,domain_file):
		self.parse(domain_file)


	def parse(self,file):
		current_element = ''
		i = 0
		#Number of parantheses pointing left or right
		num_par_left = 0
		num_par_right = 0

		#nprl is one because the first parenthese shall be accounted for
		num_par_right_last = 1
		num_par_left_last = 0

		#Number of elements in the domain file. Actions, predicates, requirecements
		num_elements = 0

		lines = []
		element = []
		for line in file:
			lines.append(line)

			i = i + 1
			#Remove whitespace
			line = line.replace(' ','')
			line = line.replace('	','')
			line = line.strip()
			

			if line:
				#if comment line
				if line[0]==";":
					continue

				for symbol in line:
					element.append(symbol)
					if symbol=='(':
						num_par_right += 1

					elif symbol ==')':
						num_par_left +=1

					
					#If the number of parantheses has changed
					if not (num_par_right_last == num_par_right) or not (num_par_left_last== num_par_left):
						
						if num_par_right-num_par_left==1:
							num_elements+=1
							self.set_element(element)
							element = []
							#print 'new',i,line

					num_par_left_last = num_par_left
					num_par_right_last = num_par_right


				

		if (num_par_right-num_par_left):
			print 'Paranthese error'
			#print line
			
	def set_element(self,element):
		element = "".join(element)
		element = element.lower()
		#print element,'\n'

		
		if element[1:7]=='define':
			self.domain_name = element[14:-1]
			#raise ValueError('Error in:',element)
		
		elif element[1:14]==':requirements':
			self.requirements = element[15:21]
			if self.requirements!='strips':
				raise ValueError('Error in: ',element,"Wrong requirements, must be strips")
		
		elif element[1:12]==':predicates':
			#print element
			self.set_predicates(element[12:-1])

		elif element[1:8]==':action':
			self.actions.append(Action(element[8:-1]))

	def set_predicates(self,element):
		predicates = get_elements(element)
		for predicate in predicates:
			self.predicates.append(Predicate(predicate[1:-1]))


def get_elements(line):

	num_par_left = 0
	num_par_right = 0

	#nprl is one because the first parenthese shall be accounted for
	num_par_right_last = 0
	num_par_left_last = 0
	element=[]
	elements = []
	num_elements = 0
	for symbol in line:
		element.append(symbol)
		if symbol=='(':
			num_par_right += 1

		elif symbol ==')':
			num_par_left +=1

		
		#If the number of parantheses has changed
		if not (num_par_right_last == num_par_right) or not (num_par_left_last== num_par_left):
			
			if num_par_right-num_par_left==0:
				num_elements+=0
				elements.append(element)
				element = []
				#print 'new',i,line

		num_par_left_last = num_par_left
		num_par_right_last = num_par_right
	return elements

def main():

	debug = False

	domain_file_name = 'C:\Users\Magnus\Documents\Planning\probs\\satellite\domain.pddl'
	#domain_file_name = 'C:\Users\Magnus\Documents\Planning\probs\\blocks\domain.pddl'

	domain_file = open(domain_file_name,'r')

	try:
		domain = Domain(domain_file)
	except ValueError as err:
		print '------------------'
		for arg in err.args:
			print arg
		print '------------------'
	domain_file.close()


	

	if debug:
		for predicate in domain.predicates:
			print predicate.name
			print predicate.parameters

		for action in domain.actions:
			print action.name
			for precondition in action.preconditions:
				print '---------------'
				print precondition.name
				print precondition.parameters
		

if __name__=='__main__':
	main()