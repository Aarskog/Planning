import numpy as np
import copy
import random
from Queue import Queue

class board:
    def __init__(self,parent_board = None,action=None):
        self.boardsize = 3
        self.pos_actions = []
        if parent_board is None:
            #First board; intitialize with a random board
            self.board = np.reshape(random.sample(range(self.boardsize**2), self.boardsize**2),(-1,self.boardsize))
        else:
            self.board =  copy.deepcopy(parent_board.board)
            self.get_new_board(action,parent_board)
        possible_actions()

    def is_solved(self):
        solution = [[0,1,2],[3,4,5],[6,7,8]]

    def possible_actions(self):
        zero_position = np.argwhere(self.board==0)[0]
        if zero_position[0]>0:
            self.pos_actions.append(board(parent_board=self,action='down'))

        if zero_position[0]<self.boardsize:
            self.pos_actions.append(board(parent_board=self,action='up'))

        if zero_position[1]>0:
            self.pos_actions.append(board(parent_board=self,action='right'))

        if zero_position[1]<self.boardsize:
            self.pos_actions.append(board(parent_board=self,action='left'))


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

    q = Queue
    visited = []
    path = []

    init_board = board()
    q.put(init_board)

def main():
    board1 = board()
    #board1.possible_actions()
    board2 = board(parent_board=board1,action='left')
    #boards.print_board()
    #boards.possible_actions()



    #bfs_solve()


if __name__ == "__main__":
    main()
