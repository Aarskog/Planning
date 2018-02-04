import numpy as np
import copy
import random


class board:
    board = []
    boardsize = 3
    pos_actions = []

    def __init__(self,parent_board = None,action=None):
        #self.boardsize = 3
        self.pos_actions = []
        if parent_board is None:
            #First board; intitialize with a random board
            self.board = np.array(np.reshape(random.sample(range(self.boardsize**2), self.boardsize**2),(-1,self.boardsize)))
            #self.board = np.array([[3,1,2],[6,4,5],[0,7,8]])
        else:
            self.board =  copy.deepcopy(parent_board.board)
            self.get_new_board(action,parent_board)


    def is_solved(self):
        solution = np.array([[0,1,2],[3,4,5],[6,7,8]])
        return (self.board == solution).all()

    def possible_actions(self):
        zero_position = np.argwhere(self.board==0)[0]

        if zero_position[0]>0:
            self.pos_actions.append(board(parent_board=self,action='down'))

        if zero_position[0]<(self.boardsize-1):
            self.pos_actions.append(board(parent_board=self,action='up'))

        if zero_position[1]>0:
            self.pos_actions.append(board(parent_board=self,action='right'))

        if zero_position[1]<(self.boardsize-1):
            self.pos_actions.append(board(parent_board=self,action='left'))
        return self.pos_actions

    def get_new_board(self,action,parent_board):
        zero_position = np.argwhere(self.board==0)[0]
        if action=='down':
            #Swap
            self.board[zero_position[0]][zero_position[1]],self.board[zero_position[0]-1][zero_position[1]] = parent_board.board[zero_position[0]-1][zero_position[1]],parent_board.board[zero_position[0]][zero_position[1]]

        elif action=='up':
            self.board[zero_position[0]][zero_position[1]],self.board[zero_position[0]+1][zero_position[1]] = parent_board.board[zero_position[0]+1][zero_position[1]],parent_board.board[zero_position[0]][zero_position[1]]

        elif action == 'right':
            self.board[zero_position[0]][zero_position[1]],self.board[zero_position[0]][zero_position[1]-1] = parent_board.board[zero_position[0]][zero_position[1]-1],parent_board.board[zero_position[0]][zero_position[1]]

        elif action == 'left':
            self.board[zero_position[0]][zero_position[1]],self.board[zero_position[0]][zero_position[1]+1] = parent_board.board[zero_position[0]][zero_position[1]+1],parent_board.board[zero_position[0]][zero_position[1]]



def bfs_solve():

    visited = []
    #path = []

    init_board = board()
    q = [init_board]

    i = 0

    while q:
        possible_solution = q.pop()

        if possible_solution.is_solved():
            print i
            print possible_solution.board
            return 'solved',i

        else:
            new_nodes = possible_solution.possible_actions()

            for new_node in new_nodes:
                is_visited = False
                for visited_node in visited:
                    if (new_node.board==visited_node).all():
                        is_visited = True
                        break

                if not is_visited:
                    q.insert(0,new_node)
        visited.append(possible_solution.board)
        #print possible_solution.board
        print i
        i = i + 1


def main():
    #board1 = board()
    #solution = np.array([[0,1,2],[3,4,5],[6,7,8]])
    #print solution
    # print board1.board
    # print (solution==solution)

    # pos_ac = board1.possible_actions()
    # print board1.board
    # for board_item in pos_ac:
    #     print board_item.board
    #board2 = board(parent_board=board1,action='left')
    #boards.print_board()
    #boards.possible_actions()

    #print bfs_solve()

    print bfs_solve()


if __name__ == "__main__":
    main()
