import copy

class PlayGame:
    def __init__(self, board):
        self.board = board

    # A method which will take number of iterations and call other methods
    def playTheGame(self, n):
        print("Original set up:")
        self.drawBoard()

        for i in range(n):
            self.interactions()
            print()
            print("Iteration:", i + 1)
            self.drawBoard()

    def drawBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    print("[ ]", end='')
                if self.board[i][j] == 1:
                    print("[o]", end='')
            print()

            #run iteration
    def interactions(self):
        # If the board needs extending then extend it as new cells will be created outisde the current board
        if self.checkIfBoardNeedsExtending() == True:
            self.extendBoard()
            self.extendBoard()

        # Creating a copy of the board so that while I update the board this doesnt
        # affect cells which should/shouldn't be killed but aren't/are
        temp_board = copy.deepcopy(self.board)

        # Now we need to perform nine different pieces of code but together they pass through
        # the whole board. The problem is for the edge cases we can't check e.g whether board[i+1]
        # has a cell as this will give a list index out of age error. So we have 9 different cases:
        # the 4 corners, first and last rows and columns and the 'middle' of the board

        # For the middle of the board (start index at 1 and end at len-2):
        for i in range(1,len(temp_board)-1):
            for j in range(1,len(temp_board[i])-1):
                # For each position check for and keep count of neighbouring cells
                count = 0

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

                # If this current position is a cell and count is <2 or >3 then cell dies
                if (temp_board[i][j] == 1) and (count < 2 or count > 3):
                    self.board[i][j] = 0
                # If this current position is empty and there a 3 cells neighbouring cell is created
                if (temp_board[i][j] == 0) and count == 3:
                    self.board[i][j] = 1
                # otherwise do nothing

        return self.board

    # Create a method which will extend the board when called
    def extendBoard(self):
        num_rows = len(self.board)
        num_columns = len(self.board[0])

        for i in range(num_rows):
            self.board[i].append(0)
            self.board[i].insert(0, 0)

        self.board.append([0] * (num_columns + 2))
        self.board.insert(0, [0] * (num_columns + 2))

        return self.board

    # Create a method to check if need to extend the board
    def checkIfBoardNeedsExtending(self):
        num_rows = len(self.board)
        num_columns = len(self.board[0])

        # Idea is to check if there are any cells (1s) on the edge, if there
        # are then return True as we will need an extra row of zeros
        for i in range(0, 1):
            for j in range(num_columns):
                if self.board[i][j] == 1:
                    return True

        for i in range(num_rows - 1, num_rows):
            for j in range(num_columns):
                if self.board[i][j] == 1:
                    return True

        for i in range(num_rows):
            for j in range(0, 1):
                if self.board[i][j] == 1:
                    return True

        for i in range(num_rows):
            for j in range(num_columns - 1, num_columns):
                if self.board[i][j] == 1:
                    return True

        return False #since by now if there were no cells we dont need to extend the board


if __name__ == '__main__':
    board1 = [[1,0,1,0,0,1,0],[0,1,1,1,0,1,1],[0,1,1,0,1,0,1],[1,0,0,1,0,0,1],[1,1,0,0,1,0,0],[1,1,0,0,1,1,0],[1,1,1,0,0,1,0]]
    board2 = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]] # beacon (period 2)
    board3 = [[0,0,0,0],[0,1,1,1],[1,1,1,0],[0,0,0,0]] # toad (period 2)
    board4 = [[0,0,0],[1,1,1],[0,0,0]] # blinker (period 2)
    board5 = [[0,0,1,1,1,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,1,0,0,0,0,1],[1,0,0,0,0,1,0,1,0,0,0,0,1],[0,0,1,1,1,0,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,1,1,1,0,0],[1,0,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,1,0,0,0,0,1],[1,0,0,0,0,1,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,1,1,1,0,0]] # pulsar (period 3)
    # game1 = PlayGame(board1)
    # game1.playTheGame(4)
    game2 = PlayGame(board5)
    # game2.drawBoard()
    game2.playTheGame(5)
