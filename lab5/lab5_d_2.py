from Tkinter import *
import random
from math import *

# Helper functions

def draw_star(can, color, radius, x_coord, y_coord, number_points):
    '''Takes 6 arguments: can the canvas to draw on, color, the radius of the 
    circle the star is contained within, x_coord the x coordinate of the center 
    of the star, y_coord the y coordinate of the center of the circle, and
    number_points the number of points that the star has. Draws a star of 
    the color specified centered at (x_coord, y_coord) with the designated 
    radius and the designated number_points.
    '''
    star = []
    theta = (2 * pi) / number_points
    point_lst = []
    for i in range(number_points):
        point_lst.append(i)
        if i + (number_points - 1) / 2 >= number_points:
            point_lst.append(i + (number_points - 1) / 2 - number_points)
        else:
            point_lst.append(i + (number_points - 1) / 2)
    for j in range(number_points):
        point_1 = point_lst.pop(0)
        point_2 = point_lst.pop(0)
        line = can.create_line(x_coord + radius * sin(theta * point_1), \
                               y_coord - radius * cos(theta * point_1), \
                               x_coord + radius * sin(theta * point_2), \
                               y_coord - radius * cos(theta * point_2), \
                               fill = color)
        star.append(line)    
    global star_lst
    star_lst.append(star)
    
def random_color():
    '''Generates random color values in the format of #RRGGBB.
    '''
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', \
                'c', 'd', 'e', 'f']
    color = '#'
    for a in range(6):
        color += random.choice(hex_list)
    return color

def random_diameter():
    '''Returns a random even number between 50 and 100 to be used as the 
    diameter for a circle.
    '''
    return 2 * (random.randint(25, 50))

# Event handlers

def key_handler(event):
    '''Handle key presses.'''
    global n
    if event.keysym == 'q':
        quit()
    elif event.keysym == 'c':
        global current_color
        current_color = random_color()
    elif event.keysym == 'x':
        global star_lst
        for star in star_lst:
            for line in star:
                canvas.delete(line)
        star_lst = []
    elif event.keysym == 'plus':
        n += 2
    elif event.keysym == 'minus':
        if n > 5:
            n -= 2
    
        
def button_handler(event):
    '''Handle left mouse button click events.'''
    global current_color
    global n
    draw_star(canvas, current_color, random_diameter() / 2, event.x, event.y, n)

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    current_color = random_color() 
    star_lst = []
    n = 5
    
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    root.mainloop()
