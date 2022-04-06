from tkinter import *
import time


class GameSimulation:
    def __init__(self, canvas, row, column, width, height):
        """
       c - canvas instance
       r - number of rows
       c - number of columns
       width - width of game field in pixels
       height - width of game field in pixels
       """
        self.canvas = canvas
        self.row = row + 3
        self.column = column + 3
        self.width = width
        self.height = height
        self.a = [[1 if not i % 9 else 0 for i in range(self.width)] for j in range(self.height)]
        self.__animate()

    def __step(self):
        b = []
        for i in range(self.width):
            b.append([])
            for j in range(self.height):
                b[i].append(0)

        for i in range(1, self.row - 1):
            for j in range(1, self.column - 1):
                neighbours = self.a[i - 1][j - 1] + self.a[i - 1][j] + self.a[i - 1][j + 1] + self.a[i][j - 1] + \
                           self.a[i - 1][j + 1] + self.a[i + 1][j - 1] + self.a[i + 1][j] + self.a[i + 1][j + 1]
                if neighbours < 2 or neighbours > 3:
                    b[i][j] = 0
                elif neighbours == 3:
                    b[i][j] = 1
                else:
                    b[i][j] = self.a[i][j]
        self.a = b

        try:
            time.sleep(0.2)
        except KeyboardInterrupt:
            print("Game of Life")
            print('By Ademi ademi.niiazbekkyzy@alatoo.edu.kg')

    def __animate(self):
        size_rows = self.width // (self.row - 2)
        size_columns = self.height // (self.column - 2)
        for i in range(1, self.row - 1):
            for j in range(1, self.column - 1):
                if self.a[i][j] == 1:
                    color = "blue"
                else:
                    color = "white"
                self.canvas.create_rectangle((i - 1) * size_rows, (j - 1) * size_columns, i * size_rows,
                                             j * size_columns, fill=color)
        self.__step()
        self.canvas.after(100, self.__animate)

    def show_field(self):
        for i in range(self.row):
            for j in range(self.column):
                print(self.a[i][j], end="")
            print()


root = Tk()
root.geometry("790x700")
root.title("Game Simulation")
canvas = Canvas(root, width=800, height=800)
canvas.pack()

field = GameSimulation(canvas, 60, 60, 800, 800)
field.show_field()
root.mainloop()
