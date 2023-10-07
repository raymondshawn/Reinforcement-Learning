import tkinter as tk
import random
import time
import math
class GridWindow():
    def __init__(self, rows, columns):
        super().__init__()
        self.rows = rows
        self.columns = columns
        self.cells = []  # List to store the buttons and values
        self.window=tk.Tk()
        self.clicked_cell = None         

    def on_cell_click(self, row, column):
        #print("click")
        self.clicked_cell = (row, column)
        self.update_clicked_cell_value()

    def update_clicked_cell_value(self):
        if self.clicked_cell:
            
            row, column = self.clicked_cell
            self.cells[row][column][0].configure(bg="blue",fg="blue")
            #value = self.cells[row][column][1]
            #new_value = int(value.get()) + 1
            #value.set(new_value)

    def get_clicked_cell_value(self):
        if self.clicked_cell:
            row, column = self.clicked_cell
            return self.cells[row][column][1].get()
        else:
            return None
    def run(self):
        self.window.mainloop()
    
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
                button = tk.Button(self.window, textvariable=value, padx=50, pady=50, relief=tk.RIDGE,command=lambda r=i, c=j: self.on_cell_click(r, c))
                button.grid(row=i, column=j)
                
                row.append((button, value))
            self.cells.append(row)
        return self.cells
        
       

    def get_cell_value(self, row, column):
        return self.cells[row][column][1].get()

    def set_cell_value(self, row, column, value):
        self.cells[row][column][1].set(value)
        


# Create an instance of GridWindow with 4 rows and 4 columns
grid_window = GridWindow(4, 4)
#grid=grid_window.create_grid()




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
        self.finished=False
    def run(self):
        self.window.mainloop()        
    def play(self):
        row=0
        col=0
        start_cell=self.grid[row][col][0]
            
        start_cell.invoke()
        while True:
            self.window.update()
            
            target=(3,3)
            right=(row,col+1)
            left=(row,col-1)
            up=(row+1,col)
            down=(row-1,col)
            
            up_distance=math.dist(up,target)
        
            down_distance=math.dist(down,target)
            right_distance=math.dist(right,target)
            left_distance=math.dist(left,target)
            distances={'up':up_distance,'down':down_distance,'right':right_distance,'left':left_distance}
            key_with_smallest_value = min(distances, key=distances.get)
            if row==3 and col==3:
                print(f"end {row,col}")
                break
            elif key_with_smallest_value=='up':
                row,col=up[0],up[1]
            elif key_with_smallest_value=='down':
                row,col=down[0],down[1]
            elif key_with_smallest_value=='right':
                row,col=right[0],right[1]
            elif key_with_smallest_value=='left':
                row,col=left[0],left[1]
            
            random_cell=self.grid[row][col][0]
            
            random_cell.invoke()
            
            
            print(f'in play {row,col}')
            time.sleep(3)  
            
    def end(self):
        pass
    
    
game=Game(grid_window)
#game.play()

game.play()
game.run()