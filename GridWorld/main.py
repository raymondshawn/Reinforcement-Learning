import tkinter as tk

# Create the main window
window = tk.Tk()

# Create a 4x4 grid of labels
for i in range(4):
    for j in range(4):
        label = tk.Label(window, padx=40, pady=40, relief=tk.RIDGE)
        label.grid(row=i, column=j)

# Run the main event loop
window.mainloop()