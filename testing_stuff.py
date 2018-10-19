import copy
from turtle import *
#
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(140)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


#Below worked
def interactions(self):
    temp_board = copy.deepcopy(self.board)

    for i in range(len(temp_board)):
        for j in range(len(temp_board)):

            if temp_board[i][j] == 1:

                print("i:",i,'j:',j)
                if self.cellDeath(i,j) == True:
#IMPORTANT, had an error here because when calling the method I was not using self but just cellDeath
                    self.board[i][j] = 0
                    print("self: ", self.board)
                    print("temp:", temp_board)

    return self.board

def cellDeath(self, i, j):
    count = 0

    if self.board[i-1][j-1] == 1:
        count += 1
    if self.board[i-1][j] == 1:
        count += 1
    if self.board[i-1][j+1] == 1:
        count += 1
    if self.board[i][j-1] == 1:
        count += 1
    if self.board[i][j+1] == 1:
        count += 1
    if self.board[i+1][j-1] == 1:
        count += 1
    if self.board[i+1][j] == 1:
        count += 1
    if self.board[i+1][j+1] == 1:
        count += 1
    print("count:", count)
    if count < 2 or count > 3:
        return True
    return False
