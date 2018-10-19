from PIL import Image, ImageDraw

if __name__ == '__main__':

    board = [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]

    horiz_step_count = len(board[0])
    vert_step_count = len(board)
    width = 600
    height = 600

    image = Image.new(mode='L', size=(width, height), color=255)

    # Draw a line
    draw = ImageDraw.Draw(image)

    horiz_step_size = int(image.width / horiz_step_count)
    vert_step_size = int(image.height / vert_step_count)

    y_start = 0
    y_end = image.height

    for x in range(0, image.width, horiz_step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, vert_step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)

    for i in range(len(board)):
        for j in range(len(board[i])):

            if board[i][j] == 1:
                draw.ellipse((j * vert_step_size, i * horiz_step_size, (j+1) * vert_step_size, (i+1) * horiz_step_size), fill = 'red', outline ='red')

    del draw

    image.show()
