
class PlayGame:
    def __init__(self, board):
        self.board = board

    def drawBoard(self):
        return self.board

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

if __name__ == '__main__':
    # print("  _")
    # print("|","_","|")
    # print("|","_","|")
    board = [[1,0,1,0],[0,1,1,1],[0,1,1,0],[1,0,0,1]]
    game1 = PlayGame(board)
    game1.interactions()
