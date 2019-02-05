from Tkinter import *

def draw_square(can, color, len, cent):
    '''Takes 4 arguments: can the canvas to draw on, color, len the height and 
    width of the square, and cent the center of the square. Draws a square of 
    the color specified centered at cent with dimensions len x len.
    '''
    can.create_rectangle(cent[0] - (len / 2), cent[1] - (len / 2), cent[0]\
                         + (len / 2) + 1, cent[1] + (len / 2) + 1, fill = color\
                         , outline = color)

if __name__ == '__main__':

    root = Tk()
    canvas = Canvas(root, width = 800, height = 800)
    canvas.pack()
    draw_square(canvas, 'red', 100, (50, 50))
    draw_square(canvas, 'green', 100, (750, 50))
    draw_square(canvas, 'blue', 100, (50, 750))
    draw_square(canvas, 'yellow', 100, (750, 750))

    root.mainloop()