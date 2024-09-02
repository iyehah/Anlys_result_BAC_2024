import tkinter as tk
from tkinter import messagebox
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from main import DataVisualizer

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        sys.exit()

# Create the main application window
root = tk.Tk()
root.title("Analyse Results BAC 2024")
root.geometry("1200x600")

# Bind the window close event to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)

# Create a DataVisualizer instance
visualizer = DataVisualizer("BAC.xlsx")

# Create and place the Serie Diagram in a frame
frame_serie = tk.Frame(root)
frame_serie.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
serie_figure = visualizer.create_serie_diagram()
canvas_serie = FigureCanvasTkAgg(serie_figure, master=frame_serie)
canvas_serie.draw()
canvas_serie.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create and place the Lregf Diagram in another frame
frame_lregf = tk.Frame(root)
frame_lregf.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
lregf_figure = visualizer.create_lregf_diagram()
canvas_lregf = FigureCanvasTkAgg(lregf_figure, master=frame_lregf)
canvas_lregf.draw()
canvas_lregf.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Calculate and display the max and min Moybac in labels
frame_max_min = tk.Frame(root)
frame_max_min.pack(side=tk.BOTTOM, fill=tk.X)
max_value, max_name, min_value, min_name = visualizer.calculate_max_min()
max_label = tk.Label(frame_max_min, text=f"Maximum Moybac: {max_value} (Name: {max_name})")
min_label = tk.Label(frame_max_min, text=f"Minimum Moybac: {min_value} (Name: {min_name})")
max_label.pack(side=tk.LEFT)
min_label.pack(side=tk.RIGHT)

# Run the application
root.mainloop()
