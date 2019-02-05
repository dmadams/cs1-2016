# Sorry about the line endings. I forgot to put my settings on sublime back to
# normal. They should be fixed now.

from Tkinter import *

root = Tk()
canvas = Canvas(root, width = 800, height = 800)
canvas.pack()
canvas.create_rectangle(0, 0, 101, 101, fill = 'red', outline = 'red')
canvas.create_rectangle(700, 0, 801, 101, fill = 'green', outline = 'green')
canvas.create_rectangle(0, 700, 101, 801, fill = 'blue', outline = 'blue')
canvas.create_rectangle(700, 700, 801, 801, fill = 'yellow', outline = 'yellow')

root.mainloop()