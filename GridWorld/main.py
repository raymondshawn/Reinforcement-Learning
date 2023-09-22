import tkinter as tk
from tkinter import font,messagebox
import random
import time
class GridWindow():
    def __init__(self, rows, columns):
        super().__init__()
        self.rows = rows
        self.columns = columns
        self.cells = []  # List to store the buttons and values
        self.window=tk.Tk()
        


    def run(self):
        self.window.mainloop()
    def button_click(self,row,col):
        #print(self.get_cell_value(row,column))
        print(row,col)
       
        print(f"event click")
    def create_grid(self):
        # Create the main window
       

        # Define a larger font size
        # custom_font = font.Font(size=14)

        # Create a grid of buttons with specified number of rows and columns
        for i in range(self.rows):
            row = []  # List to store buttons and values in a row
            for j in range(self.columns):
                value = tk.StringVar()  # Variable to hold the value of the cell
                value.set(0)  # Set initial value to zero
                button = tk.Button(self.window, textvariable=value, padx=50, pady=50, relief=tk.RIDGE,command=lambda r=i, c=j: self.button_click(r, c))
                button.grid(row=i, column=j)
                
                row.append((button, value))
            self.cells.append(row)
        return self.cells
        # Run the main event loop
       

    def get_cell_value(self, row, column):
        return self.cells[row][column][1].get()

    def set_cell_value(self, row, column, value):
        self.cells[row][column][1].set(value)
        


# Create an instance of GridWindow with 4 rows and 4 columns
grid_window = GridWindow(4, 4)
grid=grid_window.create_grid()




"""
# Access and modify a cell in the grid
cell_2_3_value = grid_window.get_cell_value(1, 2)
print(cell_2_3_value)  # Prints the value of the cell at row 2, column 3

grid_window.set_cell_value(1, 2, 5)  # Set the value of the cell at row 2, column 3 to 5
updated_value = grid_window.get_cell_value(1, 2)
print(updated_value)  # Prints the updated value of the cell at row 2, column 3
"""

class Game:
    def __init__(self,gridwindow:GridWindow):
        super().__init__()
        self.grid_window=gridwindow
        self.window=self.grid_window.window
        self.grid=gridwindow.create_grid()
        self.goal=self.grid[3][3]
        self.clicked=None
        self.finished=False
    def run(self):
        self.window.mainloop()        
    def play(self):
        
        while True:
            self.window.update()
            row=random.randint(0,3)
            col=random.randint(0,3)
            if row==3 and col==3:
                print(f"end {row,col}")
                break
            random_cell=self.grid[row][col][0]
            #self.window.after(0,random_cell.invoke)
            random_cell.invoke()
            random_cell.configure(background="blue")
            
            print(f'in play {row,col}')
            time.sleep(3)  
            
    def end(self):
        pass
    
    
game=Game(grid_window)
#game.play()

game.play()
game.run()