import copy
import time
from PIL import Image, ImageDraw

class GameOfLife:
    '''This is the Game of Life class. It takes as input an object board which is
    a 2D array of 1s and 0s, where the 0 represents a dead cell and 1 an alive cell.
    To alter the initial configuration of cells do so in the main function outside this class'''

    # Constructor - creating an instance variable - board
    def __init__(self, board):
        self.board = board

    # Main play the game method which will take in number of iterations and draw
    # the board after each iteration
    def playTheGame(self, n):
        print("Welcome to the Game of Life!")
        self.drawBoard()

        for i in range(n):
            self.runIteration()
            self.drawBoard()

    # This method will draw the board
    def drawBoard(self):
        horiz_step_count = len(self.board[0]) # number of columns
        vert_step_count = len(self.board) # number of rows
        width = 600
        height = 600

        # Create an image (white square) of size widthxheight:
        image = Image.new(mode='L', size=(width, height), color=255)

        # First draw the grid by drawing the required number of lines:
        draw = ImageDraw.Draw(image)

        # Need to set the the seperation of the lines:
        horiz_step_size = int(image.width / horiz_step_count)
        vert_step_size = int(image.height / vert_step_count)

        y_start = 0
        y_end = image.height

        # line =((a,b),(c,d)) creates a line from (a,b) to (c,d)
        for x in range(0, image.width, horiz_step_size):
            line = ((x, y_start), (x, y_end))
            draw.line(line, fill=128)

        x_start = 0
        x_end = image.width

        for y in range(0, image.height, vert_step_size):
            line = ((x_start, y), (x_end, y))
            draw.line(line, fill=128)

        # Now draw the cells:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):

                if self.board[i][j] == 1:
                    draw.ellipse((j * vert_step_size, i * horiz_step_size, (j+1) * vert_step_size, (i+1) * horiz_step_size), fill = 'red', outline ='red')

        del draw
        image.show()

    # This method will run a single iteration
    def runIteration(self):
        # If the board needs extending then extend it as new cells will have to
        # be created outisde the current board
        if self.checkIfBoardNeedsExtending() == True:
            self.extendBoard()
            self.extendBoard()

        # Creating a copy of the board so that it doesn't matter whether a cells
        # first die or are born, everything happens simultaneously each iteration.
        temp_board = copy.deepcopy(self.board)

        # Go through the whole board except the edges since there will always be
        # an extra layer of dead cells that won't become alive in a given iteration
        for i in range(1,len(temp_board)-1):
            for j in range(1,len(temp_board[i])-1):

                count = self.getNumberOfAliveNeighbours(temp_board, i, j)

                # If the current cell is alive and we have either underpopulation
                # or overcrowding the cell dies
                if (temp_board[i][j] == 1) and (count < 2 or count > 3):
                    self.cellDies(i, j)

                # If the current cell is dead and we have exactly 3 alive neighbours
                # this cell becomes alive
                if (temp_board[i][j] == 0) and count == 3:
                    self.cellCreated(i, j)

        return self.board

    # This method will return the number of alive neighbouring cells for a cell in
    # a given row and column.
    def getNumberOfAliveNeighbours(self, temp_board, row, column):
        # Initialise count
        count = 0

        # For each of the eight neighbouring cells check if they are alive and
        # increment count if they are:
        if temp_board[row-1][column-1] == 1:
            count += 1
        if temp_board[row-1][column] == 1:
            count += 1
        if temp_board[row-1][column+1] == 1:
            count += 1
        if temp_board[row][column-1] == 1:
            count += 1
        if temp_board[row][column+1] == 1:
            count += 1
        if temp_board[row+1][column-1] == 1:
            count += 1
        if temp_board[row+1][column] == 1:
            count += 1
        if temp_board[row+1][column+1] == 1:
            count += 1

        return count

    # Kill a cell in a given position
    def cellDies(self, row, column):
        self.board[row][column] = 0

    # Create a cell in a given position
    def cellCreated(self, row, column):
        self.board[row][column] = 1

    # A method which will extend the board when called
    def extendBoard(self):
        num_rows = len(self.board)
        num_columns = len(self.board[0])

        # First add an extra zero at the begging and end of each row
        for i in range(num_rows):
            self.board[i].append(0)
            self.board[i].insert(0, 0)

        # Then create an extra two rows (at the top and bottom) of zeros, the size of
        # these rows is now the number of columns of previous board plus two.
        self.board.append([0] * (num_columns + 2))
        self.board.insert(0, [0] * (num_columns + 2))

        return self.board

    # A method to check if board needs to be extended
    def checkIfBoardNeedsExtending(self):
        num_rows = len(self.board)
        num_columns = len(self.board[0])

        # Idea is to check if there are any cells (1s) on the edge, if there
        # are then return True as we will need an extra row of zeros. We go
        # through each edge seperately:
        for i in range(0, 2):
            for j in range(num_columns):
                if self.board[i][j] == 1:
                    return True

        for i in range(num_rows - 2, num_rows):
            for j in range(num_columns):
                if self.board[i][j] == 1:
                    return True

        for i in range(num_rows):
            for j in range(0, 2):
                if self.board[i][j] == 1:
                    return True

        for i in range(num_rows):
            for j in range(num_columns - 2, num_columns):
                if self.board[i][j] == 1:
                    return True

        return False #since by now if there were no cells we dont need to extend the board


''' Main function where we instantiate the class'''

if __name__ == '__main__':
    board1 = [[1,0,1,0,0,1,0],[0,1,1,1,0,1,1],[0,1,1,0,1,0,1],[1,0,0,1,0,0,1],[1,1,0,0,1,0,0],
    [1,1,0,0,1,1,0],[1,1,1,0,0,1,0]] # random board
    # Periodic solutions:
    board2 = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]] # beacon (period 2)
    board3 = [[0,0,0,0],[0,1,1,1],[1,1,1,0],[0,0,0,0]] # toad (period 2)
    board4 = [[0,0,0],[1,1,1],[0,0,0]] # blinker (period 2)
    board5 = [[0,0,1,1,1,0,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,1,0,0,0,0,1],[1,0,0,0,0,1,0,1,0,0,0,0,1],[0,0,1,1,1,0,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,1,1,1,0,0],[1,0,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,0,0,0,1,0,1,0,0,0,0,1],[1,0,0,0,0,1,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0,1,1,1,0,0]] # pulsar (period 3)

    game2 = GameOfLife(board5)
    game2.playTheGame(8)
