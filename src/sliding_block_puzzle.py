import numpy as np
import copy
import random
import time
import collections

class board:
    board = []
    boardsize = 3
    pos_actions = []


    def __init__(self,parent_board = None,action=None):
        #self.boardsize = 3
        self.action = action
        self.pos_actions = []
        self.parent_board = parent_board
        self.solution = np.array(np.reshape(range(self.boardsize**2),(-1,self.boardsize)))

        if parent_board is None:
            #First board; intitialize with a random board
            self.board = np.array(np.reshape(random.sample(range(self.boardsize**2), self.boardsize**2),(-1,self.boardsize)))
            #self.board = np.array([[1,2,5],[4,6,8],[3,7,0]])
            #self.board = np.array([[0,2,5],[1,6,3],[7,8,4]])
            #self.board = np.array([[2,0,1],[4,7,8],[6,3,5]])
            self.h = self.h_manhattan_distance()
            self.depth = 0

        else:
            self.board =  copy.deepcopy(parent_board.board)
            self.do_action(action)

            self.depth = parent_board.depth + 1
            #self.h_total = self.h_manhattan_distance()+copy.deepcopy(parent_board.h)
            self.h = self.h_manhattan_distance() + self.depth

    def is_solved(self):
        return (self.board == self.solution).all()

        #creates child nodes

    def possible_actions(self):
        zero_position = np.argwhere(self.board==0)[0]
        self.pos_actions = []
        if zero_position[0]>0: #and not self.action == 'down':
            self.pos_actions.append(board(parent_board=self,action='up'))

        if zero_position[0]<(self.boardsize-1):#and not self.action == 'up':
            self.pos_actions.append(board(parent_board=self,action='down'))

        if zero_position[1]>0: #and not self.action == 'right':
            self.pos_actions.append(board(parent_board=self,action='left'))

        if zero_position[1]<(self.boardsize-1): #and not self.action == 'left':
            self.pos_actions.append(board(parent_board=self,action='right'))
        return self.pos_actions

    def do_action(self,action):
        zero_position = np.argwhere(self.board==0)[0]
        if action=='up':
            #Swap
            self.board[zero_position[0]][zero_position[1]],self.board[zero_position[0]-1][zero_position[1]] = self.board[zero_position[0]-1][zero_position[1]],self.board[zero_position[0]][zero_position[1]]

        elif action=='down':
            self.board[zero_position[0]][zero_position[1]],self.board[zero_position[0]+1][zero_position[1]] = self.board[zero_position[0]+1][zero_position[1]],self.board[zero_position[0]][zero_position[1]]

        elif action == 'left':
            self.board[zero_position[0]][zero_position[1]],self.board[zero_position[0]][zero_position[1]-1] = self.board[zero_position[0]][zero_position[1]-1],self.board[zero_position[0]][zero_position[1]]

        elif action == 'right':
            self.board[zero_position[0]][zero_position[1]],self.board[zero_position[0]][zero_position[1]+1] = self.board[zero_position[0]][zero_position[1]+1],self.board[zero_position[0]][zero_position[1]]

    def h_misplaced_tiles(self):
        #heuristic function of number of misplaces tiles
        return np.sum(self.board!=self.solution)

    def h_manhattan_distance(self):
        h = 0
        #ex, ey = np.argwhere(self.board==0)[0]
        for i in range(1,self.boardsize**2):
            sx,sy = np.argwhere(self.board==i)[0]
            ex, ey =i/self.boardsize,i%self.boardsize


            h = h + abs(ex - sx) + abs(ey - sy)
        return h

    def execute_path(self,path):
        #print self.board
        for action in path:
            print '---------------'
            self.do_action(action)
            print action
            print self.board

def print_path(board_node):
    if not board_node.parent_board:
        return
    print_path(board_node.parent_board)
    print board_node.action

def get_path(board_node,path):
    if not board_node.parent_board:
        return board_node.action
    get_path(board_node.parent_board,path)
    #print board_node.action
    path.append(board_node.action)
    #print path

def solve2(init_board):
    #init_board.board.flags.writeable = False
    visited = {tuple(init_board.board.data):True}
    q = [init_board]

    #root = Node(init_board.h,init_board)

    i = 0
    possible_solution = init_board
    maxdepth = 0
    while q:
        #possible_solution = get_next_node(root)
        #print possible_solution.board
        possible_solution = q.pop(0)

        if possible_solution.is_solved():
            #print possible_solution.board
            #print_path(possible_solution)
            print 'Solved'
            path = []
            get_path(possible_solution,path)
            #print path
            return path


        else:
            new_nodes = possible_solution.possible_actions()

            for new_node in new_nodes:
                is_visited = False

                if tuple(new_node.board.data) in visited:
                    is_visited = True

                if not is_visited:
                    #binary_insert(root,Node(new_node.h,new_node))
                    visited[tuple(new_node.board.data)]=True

                    #Insert into sorted list
                    inserted = False
                    for k in range(0,len(q)):
                        if new_node.h <= q[k].h:
                            q.insert(k,new_node)
                            inserted = True
                            break

                    if not inserted:
                        q.insert(len(q),new_node)


            # j=0
            # posit = 0



        #visited[tuple(possible_solution.board.data)]=True
        #visited.append(possible_solution.board)

        # print 'Visited: ',len(q)
        #print '{0}\r'.format(i),

        if possible_solution.depth > maxdepth:
            maxdepth = possible_solution.depth
            print maxdepth
        #print possible_solution.depth

        # print "--------------debug------------"
        # print 'i=',i
        # print possible_solution.board
        # print 'h=', possible_solution.h
        # print "-------------------------------"
        i = i + 1
        #print len(q)


    print '---NOT SOLVABLE---'
    return []


def main():

    board_to_solve = board()
    print 'h=',board_to_solve.h
    print board_to_solve.board
    path = solve2(board_to_solve)
    print 'length of path = ',len(path)
    print path
    #board_to_solve.execute_path(path)


if __name__ == "__main__":
    main()


def solve(init_board):

    visited = []
    #path = []

    #init_board = board()
    q = [init_board]

    i = 0
    possible_solution = init_board
    while q:
        #possible_solution = get_next_node(root)
        #print possible_solution.board


        if possible_solution.is_solved():
            #print possible_solution.board
            #print_path(possible_solution)
            path = []
            get_path(possible_solution,path)
            #print path
            return path


        else:

            new_nodes = possible_solution.possible_actions()
            for new_node in new_nodes:
                is_visited = False
                for visited_node in visited:
                    if (new_node.board==visited_node).all():
                        is_visited = True
                        break
                if not is_visited:
                    #binary_insert(root,Node(new_node.h,new_node))
                    q.insert(0,new_node)

            possible_solution = q[0]
            j=0
            posit = 0
            for node in q:
                if node.h<possible_solution.h:
                    posit = j
                    possible_solution = node
                j=j+1

            del q[posit]


        visited.append(possible_solution.board)

        # print 'Visited: ',len(q)
        print '{0}\r'.format(i),

        # print "--------------debug------------"
        # print 'i=',i
        # print possible_solution.board
        # print 'h=', possible_solution.h
        # print "-------------------------------"
        i = i + 1

    print


class Node:
    def __init__(self, h,h_board):
        self.l_child = None
        self.r_child = None
        self.data = h
        self.h_board = h_board

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    #print root.data
    in_order_print(root.r_child)

def in_order_get(root):
    if not root.l_child or not root.l_child.h_board.visited:
        return root.h_board
    return in_order_get(root.l_child)
    #return root.h_board
    #in_order_get(root.r_child)

def get_next_node(root):
    if not root.l_child:
        return root.h_board
    if root.l_child:
        return get_next_node(root.l_child)
    else:
        return get_next_node(root.r_child)
