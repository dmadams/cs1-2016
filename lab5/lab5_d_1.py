from Tkinter import *
import random

# Helper functions

def draw_circle(can, color, radius, x_coord, y_coord):
    '''Takes 5 arguments: can the canvas to draw on, color, the radius of the 
    circle, x_coord the x coordinate of the center of the circle, and y_coord 
    the y coordinate of the center of the circle. Draws a circle of the color 
    specified centered at (x_coord, y_coord) with the designated radius.
    '''
    circle = can.create_oval(x_coord - radius, y_coord + radius, \
                             x_coord + radius, y_coord - radius, fill = color, \
                             outline = color)
    global circle_lst
    circle_lst.append(circle)

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
    '''Returns a random even number between 10 and 50 to be used as the diameter
    for a circle.
    '''
    return 2 * (random.randint(5, 25))

# Event handlers

def key_handler(event):
    '''Handle key presses.'''
    if event.keysym == 'q':
        quit()
    elif event.keysym == 'c':
        global current_color
        current_color = random_color()
    elif event.keysym == 'x':
        global circle_lst
        for circle in circle_lst:
            canvas.delete(circle)
        circle_lst = []
        

def button_handler(event):
    '''Handle left mouse button click events.'''
    global current_color
    draw_circle(canvas, current_color, random_diameter() / 2, event.x, event.y)

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    current_color = random_color() 
    circle_lst = []
    
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    root.mainloop()
