import tkinter as tk
import collections.deque as dq
import random

class Snake:
    def __init__(self, parent):
        self.parent = parent
        self.WIDTH = 800
        self.HEIGHT = 800
        self.CELL = 50
        self.RATE = 1000
        self.canvas = tk.Canvas(root, width=self.WIDTH, height=self.HEIGHT)
        self.parent.bind('<Ctrl-n>', self.draw_board)
        self.parent.bind('<Left>', self.tick)
        self.parent.bind('<Right>', self.tick)
        self.parent.bind('<Up>', self.tick)
        self.parent.bind('<Down>', self.tick)
        self.draw_board()
    def draw_board(self):
        self.direction = 'Right'
        self.canvas.delete(tk.ALL)
        self.squares = {(x, y):self.canvas.create_rectangle(x, y, x+self.CELL, y+self.CELL)
                            for x in range(0, self.WIDTH, self.CELL)
                            for y in range(0, self.HEIGHT, self.CELL)}
        self.empty = set(self.squares)
        coord = (self.WIDTH//2, self.HEIGHT//2)
        # the head is 0 and the tail is -1
        self.snake = dq([coord])
        self.canvas.itemconfig(self.squares[coord], fill='black')
        self.create_food()
        self.ticking = self.parent.after(self.RATE, self.tick)
    def create_food(self):
        self.food = random.choice(tuple(self.empty))
        self.empty.remove(self.food)
        self.canvas.itemconfig(self.squares[self.food], fill='red')
    def move(self, direction):
        x,y = self.snake[0]
        if direction == 'Left':
            target = x-self.CELL, y
        elif direction == 'Right':
            target = x+self.CELL, y
        elif direction == 'Up':
            target = x, y-self.CELL
        else:
            target = x, y+self.CELL
        # collision detection etc.
    def tick(self, event=None):
        if event:
            self.direction = event.keysym
            self.parent.after_cancel(self.ticking)
        self.move(self.direction)
        self.ticking = self.parent.after(self.RATE, self.tick)
    
    
    
root = tk.Tk()
snake = Snake(root)
root.mainloop()