import numpy as np
import os
import math

class Domain_rob_to_door():
	def __init__(self,world_size,robot_start,door_pos,obstacles=None,path=None):
		#Make room
		self.room = [[" " for x in range(world_size[1])] for y in range(world_size[0])]
		self.room_size = world_size

		#Set robot position
		self.room[robot_start[0]][robot_start[1]] = 'r'
		self.robot_pos = robot_start

		#Set door position
		self.room[door_pos[0]][door_pos[1]] = 'D'

		#Make each tile to waypoints and the adjacency matrix
		self.waypoints = []
		self.adjacency_waypoints = self.create_adjacency(world_size,self.waypoints)


		self.make_pddl_problem(robot_start,door_pos,obstacles,world_size,path)

	def create_adjacency(self,world_size,waypoints):
		adjacency_waypoints = np.zeros((world_size[0]*world_size[1],world_size[0]*world_size[1]))
		k = 0
		i = 0
		for row in self.room:
			j = 0
			for tile in row:
				waypoints.append('waypoint' + str(k))

				#Move up or down
				if k-world_size[1]>=0:
					adjacency_waypoints[k][k-world_size[1]] = 1
					adjacency_waypoints[k-world_size[1]][k] = 1

				if j == 0:
					adjacency_waypoints[k][k+1] = 1
					adjacency_waypoints[k+1][k] = 1

				elif j == (world_size[1]-1):
					adjacency_waypoints[k][k-1] = 1
					adjacency_waypoints[k-1][k] = 1

				else:
					adjacency_waypoints[k][k-1] = 1
					adjacency_waypoints[k-1][k] = 1
					adjacency_waypoints[k][k+1] = 1
					adjacency_waypoints[k+1][k] = 1

				k = k + 1
				j = j + 1
			i = i + 1
		return adjacency_waypoints

	def print_room(self):
		for tiles in self.get_room():
			print tiles

	def get_room(self):
		return self.room

	def make_pddl_problem(self,robot_start,door_pos,obstacles,world_size,path):
		adjacencies = self.get_adjacencies()

		#Lines contains the lines which are written to the pddl file
		lines = []

		lines.append('(define (problem rtd)')
		lines.append('(:domain robot-to-door)')
		lines.append('(:objects')
		lines.append('robot')
		lines.append('door')

		for waypoint in self.waypoints:
			lines.append(waypoint)

		lines.append(')')

		lines.append('(:init')
		lines.append('(robot robot)')
		lines.append('(door door)')
		lines.append('(handempty)')
		lines.append('(at robot waypoint' + str(world_size[1]*robot_start[0]+robot_start[1]) +  ')')


		for waypoint in self.waypoints:
			lines.append('(waypoint '+waypoint+')')
			# lines.append('(clear '+ waypoint+')')

		for adjacency in adjacencies:
			lines.append('(can-move '+adjacency[0]+' '+adjacency[1]+')')
		lines.append(')')

		lines.append('(:goal (and')
		lines.append('(at robot waypoint'+str(world_size[1]*door_pos[0]+door_pos[1])+')')

		lines.append(')))')

		self.make_pddl_file(lines,path)

	def make_pddl_file(self,lines,path):
		with open(path, 'w') as the_file:
			for line in lines:
				the_file.write(line+'\n')

	def get_adjacencies(self):
		adjacencies = []
		i = 0
		for row in self.adjacency_waypoints:
			j = 0
			for item in row:
				if item:
					adjacencies.append(['waypoint'+str(i),'waypoint'+str(j)])
				j = j + 1
			i = i + 1
		return adjacencies

	def do_action(self,action):

		spl_act = action.split()
		#print spl_act
		if spl_act[0] == 'move':

			#To waypoint
			to_wp = spl_act[-1]
			new_pos = (int(to_wp[8:])/self.room_size[1],int(to_wp[8:])%self.room_size[1])

			self.room[self.robot_pos[0]][self.robot_pos[1]],self.room[new_pos[0]][new_pos[1]] = " ","r"

			self.robot_pos=new_pos

		self.print_room()
			print '\n'
			#print to_wp[8:],int(to_wp[8:])/self.room_size[1],int(to_wp[8:])%self.room_size[1]



#
# def main():
# 	dir_path = os.path.dirname(os.path.realpath(__file__))
# 	dir_path = dir_path[:-3]
#
# 	path = dir_path+'probs/robot_to_door/problem.pddl'
#
# 	world_size = (7,7)
# 	rob_pos = (0,0)
# 	door_pos = (6,6)
#
# 	dom24 = Domain_rob_to_door(world_size,rob_pos,door_pos,path=path)
# 	dom24.print_room()
#
# if __name__=='__main__':
# 	main()
