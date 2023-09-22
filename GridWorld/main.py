import tkinter as tk
from tkinter import font
import random
class GridWindow:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cells = []  # List to store the buttons and values


    def button_click(self,event):
        #print(self.get_cell_value(row,column))
        print("click")
    def create_grid(self):
        # Create the main window
        window = tk.Tk()

        # Define a larger font size
        custom_font = font.Font(size=14)

        # Create a grid of buttons with specified number of rows and columns
        for i in range(self.rows):
            row = []  # List to store buttons and values in a row
            for j in range(self.columns):
                value = tk.StringVar()  # Variable to hold the value of the cell
                value.set(0)  # Set initial value to zero
                button = tk.Button(window, textvariable=value, padx=50, pady=50, relief=tk.RIDGE, font=custom_font)
                button.grid(row=i, column=j)
                button.bind("<Button-1>",self.button_click)
                row.append((button, value))
            self.cells.append(row)

        # Run the main event loop
        window.mainloop()

    def get_cell_value(self, row, column):
        return self.cells[row][column][1].get()

    def set_cell_value(self, row, column, value):
        self.cells[row][column][1].set(value)
        
    def play(self):
        # Generate random coordinates
        random_row = random.randint(0, 4)
        random_column = random.randint(0, 4)

# Get the randomly selected button
        random_cell = self.cells[random_row][random_column]

# Programmatically trigger the click event on the randomly selected button
        random_cell.invoke()

# Create an instance of GridWindow with 4 rows and 4 columns
grid_window = GridWindow(4, 4)

# Call the create_grid method to create the grid
grid_window.create_grid()
grid_window.play()
"""
# Access and modify a cell in the grid
cell_2_3_value = grid_window.get_cell_value(1, 2)
print(cell_2_3_value)  # Prints the value of the cell at row 2, column 3

grid_window.set_cell_value(1, 2, 5)  # Set the value of the cell at row 2, column 3 to 5
updated_value = grid_window.get_cell_value(1, 2)
print(updated_value)  # Prints the updated value of the cell at row 2, column 3
"""

class Game:
    def __init__(self,grid:GridWindow):
        self.grid=grid
        
    def play(self):
        pass
    def end(self):
        pass