from random import randint
from tkinter import *
import time


class GameSimulation:
    def __init__(self, c, row, column, width, height):

        """
       c - canvas instance
       r - number of rows
       c - number of columns
       width - width of game field in pixels
       height - width of game field in pixels
       """
        self.c = c
        self.row = row + 2
        self.column = column + 2
        self.width = width
        self.height = height
        self.count = 0
        self.a = [[1 if not i % 33 else 0 for i in range(self.column)] for j in range(self.row)]
        self.animate()

    def __step(self):
        __b = []
        for i in range(self.row):
            __b.append([])
            for j in range(self.column):
                __b[i].append(0)

        for i in range(1, self.row - 1):
            for j in range(1, self.column - 1):
                neighbour_sum = self.a[i - 1][j - 1] + self.a[i - 1][j] + self.a[i - 1][j + 1] + self.a[i][j - 1] + \
                           self.a[i - 1][j + 1] + self.a[i + 1][j - 1] + self.a[i + 1][j] + self.a[i + 1][j + 1]
                if neighbour_sum < 2 or neighbour_sum > 3:
                    __b[i][j] = 0
                elif neighbour_sum == 3:
                    __b[i][j] = 1
                else:
                    __b[i][j] = self.a[i][j]
        self.a = __b

        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            print("Conway's Game of Life")
            print('By Ademi ademi.niiazbekkyzy@alatoo.edu.kg')

    def print_field(self):
        for i in range(self.row):
            for j in range(self.column):
                print(self.a[i][j], end="")
            print()

    def animate(self):
        size_rows = self.width // (self.row - 2)
        size_columns = self.height // (self.column - 2)
        for i in range(1, self.row - 1):
            for j in range(1, self.column - 1):
                if self.a[i][j] == 1:
                    color = "orange"
                else:
                    color = "white"
                self.c.create_rectangle((i - 1) * size_rows, (j - 1) * size_columns,
                                        i * size_rows, j * size_columns, fill=color)
        self.__step()
        self.c.after(100, self.animate)


root = Tk()
root.geometry("700x700")
root.title("Game Simulation")
c = Canvas(root, width=800, height=800)
c.pack()

f = GameSimulation(c, 70, 70, 800, 800)
f.print_field()

root.mainloop()
