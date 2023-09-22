import tkinter as tk
from tkinter import font

class GridWindow:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cells = []  # List to store the buttons and values
        self.clicked_cell = None  # Variable to store the clicked cell
        self.window = tk.Tk()  # Create the main window

    def create_grid(self):
        # Define a larger font size
        custom_font = font.Font(size=14)

        # Create a grid of buttons with specified number of rows and columns
        for i in range(self.rows):
            row = []  # List to store buttons and values in a row
            for j in range(self.columns):
                value = tk.StringVar()  # Variable to hold the value of the cell
                value.set(0)  # Set initial value to zero
                button = tk.Button(self.window, textvariable=value, padx=20, pady=20, relief=tk.RIDGE, font=custom_font)
                button.grid(row=i, column=j)
                button.configure(command=lambda r=i, c=j: self.on_cell_click(r, c))
                row.append((button, value))
            self.cells.append(row)

    def run(self):
        # Run the main event loop
        self.window.mainloop()

    def on_cell_click(self, row, column):
        self.clicked_cell = (row, column)
        self.update_clicked_cell_value()

    def update_clicked_cell_value(self):
        if self.clicked_cell:
            row, column = self.clicked_cell
            value = self.cells[row][column][1]
            new_value = int(value.get()) + 1
            value.set(new_value)

            # Print the updated value on the terminal
            clicked_cell_value = self.get_clicked_cell_value()
            print(clicked_cell_value)

    def get_clicked_cell_value(self):
        if self.clicked_cell:
            row, column = self.clicked_cell
            return self.cells[row][column][1].get()
        else:
            return None

# Create an instance of GridWindow with 4 rows and 4 columns
grid_window = GridWindow(4, 4)

# Create the grid
grid_window.create_grid()

# Run the main event loop
grid_window.run()

grid_window.window.after(0, grid_window.cells[1][2][0].invoke)