from Tkinter import *
import random

def draw_square(can, color, len, cent):
    '''Takes 4 arguments: can the canvas to draw on, color, len the height and 
    width of the square, and cent the center of the square. Draws a square of 
    the color specified centered at cent with dimensions len x len.
    '''
    can.create_rectangle(cent[0] - (len / 2), cent[1] - (len / 2), cent[0]\
                         + (len / 2) + 1, cent[1] + (len / 2) + 1, fill = color\
                         , outline = color)

def random_size(low_bound, up_bound):
    '''Takes two arguments (both non-negative even integers, where the first 
    argument must be smaller than the second), and returns a random even 
    integer which is >= the lower number and <= the upper number.
    '''
    assert low_bound >= 0
    assert up_bound >= 0
    assert low_bound % 2 == 0
    assert up_bound % 2 == 0
    assert low_bound < up_bound
    out = random.randint(low_bound / 2, up_bound / 2)
    out *= 2
    assert out % 2 == 0
    return out

def random_position(max_x, max_y):
    '''Takes as its arguments two integers called max_x and max_y, both of 
    which are >= 0. It will return a random (x, y) pair, with both x >= 0 and 
    y >= 0 and with x <= max_x and y <= max_y.
    '''
    assert max_x >= 0
    assert max_y >= 0
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    return (x, y)

def random_color():
    '''Generates random color values in the format of #RRGGBB.
    '''
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',\
                'c', 'd', 'e', 'f']
    color = '#'
    for a in range(6):
        color += random.choice(hex_list)
    return color

if __name__ == '__main__':

    root = Tk()
    canvas = Canvas(root, width = 800, height = 800)
    canvas.pack()
    for a in range(50):
        draw_square(canvas, random_color(), random_size(20, 150),\
            random_position(800, 800))

    root.bind('<q>', quit)
    root.mainloop()
