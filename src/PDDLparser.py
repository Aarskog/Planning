import domain as dom

class State:
	def __init__(self,problem_file):
		self.name 		= ""
		self.domain 	= []
		self.objects 	= []
		self.state 		= []
		self.goal 		= []

		self.parse(problem_file)

	def parse(self,problem_file):
		for line in problem_file:
			print line

def main():

	# dir_path = os.path.dirname(os.path.realpath(__file__))
	# print dir_path
	# os.chdir("..\src")
	# print dir_path

	debug = False
	# debug = True


	domain_file_name = '/home/magnaars/Planning/probs/satellite/domain.pddl'
	domain_file_name = '/home/magnaars/Planning/probs/blocks/domain.pddl'

	problem_file_name = '/home/magnaars/Planning/probs/satellite/problem01.pddl'
	problem_file_name = '/home/magnaars/Planning/probs/blocks/problem.pddl'

	domain_file = open(domain_file_name,'r')
	problem_file = open(problem_file_name,'r')

	try:
		domain = dom.Domain(domain_file)
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
