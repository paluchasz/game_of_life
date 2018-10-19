import copy

class PlayGame:
    def __init__(self, board):
        self.board = board

    def drawBoard(self):
        return self.board

    def interactions(self):
        # Creating a copy of the board so that while I update the board this doesnt
        # affect cells which should/shouldn't be killed but aren't/are
        temp_board = copy.deepcopy(self.board)

# For the middle of the board (start index at 1 and end at len-2):

        for i in range(1,len(temp_board)-1):
            for j in range(1,len(temp_board[i])-1):

# If there is a cell present (==1) then check and keep count of neighbouring cells
                if temp_board[i][j] == 1:
                    count = 0
                    #print("i:",i,'j:',j)

                    if temp_board[i-1][j-1] == 1:
                        count += 1
                    if temp_board[i-1][j] == 1:
                        count += 1
                    if temp_board[i-1][j+1] == 1:
                        count += 1
                    if temp_board[i][j-1] == 1:
                        count += 1
                    if temp_board[i][j+1] == 1:
                        count += 1
                    if temp_board[i+1][j-1] == 1:
                        count += 1
                    if temp_board[i+1][j] == 1:
                        count += 1
                    if temp_board[i+1][j+1] == 1:
                        count += 1
                    #print("count:", count)
                    if count < 2 or count > 3:
                        self.board[i][j] = 0
                        #print("self: ", self.board)
                        #print("temp:", temp_board)

# Case for the first row:

        for i in range(0,1):
            for j in range(1,len(temp_board[i])-1):

                if temp_board[i][j] == 1:
                    count = 0
                    #print("i:",i,'j:',j)

                    if temp_board[i][j-1] == 1:
                        count += 1
                    if temp_board[i][j+1] == 1:
                        count += 1
                    if temp_board[i+1][j-1] == 1:
                        count += 1
                    if temp_board[i+1][j] == 1:
                        count += 1
                    if temp_board[i+1][j+1] == 1:
                        count += 1
                    #print("first row count:", count)
                    if count < 2 or count > 3:
                        self.board[i][j] = 0


# Case for the first column:
        for i in range(1,len(temp_board)-1):
            for j in range(0,1):

                if temp_board[i][j] == 1:
                    count = 0
                    #print("i:",i,'j:',j)

                    if temp_board[i-1][j] == 1:
                        count += 1
                    if temp_board[i-1][j+1] == 1:
                        count += 1
                    if temp_board[i][j+1] == 1:
                        count += 1
                    if temp_board[i+1][j] == 1:
                        count += 1
                    if temp_board[i+1][j+1] == 1:
                        count += 1
                    #print("first column count:", count)
                    if count < 2 or count > 3:
                        self.board[i][j] = 0


#Case for the last row:
        for i in range(len(temp_board)-1, len(temp_board)):
            for j in range(1,len(temp_board[i])-1):
                if temp_board[i][j] == 1:
                    count = 0
                    #print("i:",i,'j:',j)

                    if temp_board[i-1][j-1] == 1:
                        count += 1
                    if temp_board[i-1][j] == 1:
                        count += 1
                    if temp_board[i-1][j+1] == 1:
                        count += 1
                    if temp_board[i][j-1] == 1:
                        count += 1
                    if temp_board[i][j+1] == 1:
                        count += 1
                    #print("last row count:", count)
                    if count < 2 or count > 3:
                        self.board[i][j] = 0


#Case for the last column
        for i in range(1,len(temp_board)-1):
            for j in range(len(temp_board[i])-1, len(temp_board[i])):

                if temp_board[i][j] == 1:
                    count = 0
                    #print("i:",i,'j:',j)

                    if temp_board[i-1][j-1] == 1:
                        count += 1
                    if temp_board[i-1][j] == 1:
                        count += 1
                    if temp_board[i][j-1] == 1:
                        count += 1
                    if temp_board[i+1][j-1] == 1:
                        count += 1
                    if temp_board[i+1][j] == 1:
                        count += 1

                    #print("last column count:", count)
                    if count < 2 or count > 3:
                        self.board[i][j] = 0


#Case for [0,0]

        for i in range(0, 1):
            for j in range(0, 1):

                if temp_board[i][j] == 1:
                    count = 0
                    #print("i:",i,'j:',j)

                    if temp_board[i+1][j] == 1:
                        count += 1
                    if temp_board[i+1][j+1] == 1:
                        count += 1
                    if temp_board[i][j+1] == 1:
                        count += 1

                    #print("[0,0] count:", count)
                    if count < 2 or count > 3:
                        self.board[i][j] = 0


#Case for [0,len-1]

        for i in range(0, 1):
            for j in range(len(temp_board[i])-1, len(temp_board[i])):

                if temp_board[i][j] == 1:
                    count = 0
                    #print("i:",i,'j:',j)

                    if temp_board[i][j-1] == 1:
                        count += 1
                    if temp_board[i+1][j-1] == 1:
                        count += 1
                    if temp_board[i+1][j] == 1:
                        count += 1

                    #print("[0,len-1] count:", count)
                    if count < 2 or count > 3:
                        self.board[i][j] = 0


#Case for [len-1,0]

        for i in range(len(temp_board)-1, len(temp_board)):
            for j in range(0,1):

                if temp_board[i][j] == 1:
                    count = 0
                    #print("i:",i,'j:',j)

                    if temp_board[i-1][j] == 1:
                        count += 1
                    if temp_board[i-1][j+1] == 1:
                        count += 1
                    if temp_board[i][j+1] == 1:
                        count += 1

                    #print("[len-1,0] count:", count)
                    if count < 2 or count > 3:
                        self.board[i][j] = 0


#Case for [len-1,len-1]

        for i in range(len(temp_board)-1, len(temp_board)):
            for j in range(len(temp_board[i])-1, len(temp_board[i])):

                if temp_board[i][j] == 1:
                    count = 0
                    #print("i:",i,'j:',j)

                    if temp_board[i-1][j-1] == 1:
                        count += 1
                    if temp_board[i-1][j] == 1:
                        count += 1
                    if temp_board[i][j-1] == 1:
                        count += 1

                    #print("[len-1,len-1] count:", count)
                    if count < 2 or count > 3:
                        self.board[i][j] = 0

        return self.board


if __name__ == '__main__':
    # print("  _")
    # print("|","_","|")
    # print("|","_","|")
    board = [[1,0,1,0],[0,1,1,1],[0,1,1,0],[1,0,0,1]]
    game1 = PlayGame(board)
    game1.interactions()
