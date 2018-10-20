import copy
from PIL import Image, ImageDraw

class PlayGame:
    def __init__(self, board):
        self.board = board

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

# Create a function which will extend the board when called

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

# Idea is to check if for the rows/columns on the edge there are 3 cells (1s) in a row
# Go through the 4 edges in turn keeping a count of 1s resetting count in get a 0, once
# count hits 3 return True
        count = 0
        for i in range(0, 1):
            for j in range(num_columns):
                if self.board[i][j] == 1:
                    count += 1
                if self.board[i][j] == 0:
                    count = 0
                if count == 3:
                    return True

        count = 0
        for i in range(num_rows - 1, num_rows):
            for j in range(num_columns):
                if self.board[i][j] == 1:
                    count += 1
                if self.board[i][j] == 0:
                    count = 0
                if count == 3:
                    return True

        count = 0
        for i in range(num_rows):
            for j in range(0, 1):
                if self.board[i][j] == 1:
                    count += 1
                if self.board[i][j] == 0:
                    count = 0
                if count == 3:
                    return True

        count = 0
        for i in range(num_rows):
            for j in range(num_columns - 1, num_columns):
                if self.board[i][j] == 1:
                    count += 1
                if self.board[i][j] == 0:
                    count = 0
                if count == 3:
                    return True

        return False #since by now if there was no count=3 we dont want to extend the board

#playgame method which will take number of iterations and call other methods

    def playTheGame(self, n):
        self.drawBoard()
        for i in range(n):
            self.interactions()
            self.drawBoard()


if __name__ == '__main__':
    board1 = [[1,0,1,0,0,1,0],[0,1,1,1,0,1,1],[0,1,1,0,1,0,1],[1,0,0,1,0,0,1],[1,1,0,0,1,0,0],[1,1,0,0,1,1,0],[1,1,1,0,0,1,0]]
    board2 = [[1,1,1,1],[1,1,0,1],[1,1,0,1],[1,0,1,1]]
    # game1 = PlayGame(board1)
    # game1.playTheGame(4)
    game2 = PlayGame(board2)
    game2.drawBoard()
    print(game2.checkIfBoardNeedsExtending())
