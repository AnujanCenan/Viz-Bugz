import tkinter as tk        # normal
import tkinter.ttk as ttk   # themed

from constants import *
from Memory_Object import Memory_Object
from Grid_Drawing import Grid_Drawing

from LLDB_Interaction import *



window = tk.Tk()
greeting = tk.Label(text="VIZ-BUGZ")


greeting.pack()

memory_grid = tk.Canvas(
    window, 
    height=MEMORY_GRID_HEIGHT, 
    width=MEMORY_GRID_WIDTH, 
    bg="grey",
    highlightthickness=0, 
    borderwidth=0


)

print(f"Creating memory grid of size {NUM_ROWS} (rows) by {NUM_COLS} (columns)")
gd = Grid_Drawing(memory_grid)
gd.create_grid()
gd.label_memory_grid()
memory_grid.pack(side="left", padx=50)

mem_object = Memory_Object("x", "int", 3, 4, 42343123, 5)

next_memory = 92
next_memory = gd.add_memory_object(mem_object, next_memory, "red")
next_memory = gd.add_memory_object(mem_object, next_memory, "pink")

next_memory = gd.add_memory_object(mem_object, next_memory, "blue")

next_memory = gd.add_memory_object(mem_object, next_memory, "yellow")

next_memory = gd.add_memory_object(mem_object, next_memory, "green")
next_memory = gd.add_memory_object(mem_object, next_memory, "orange")

### Event Handling

def arrow_right(_: tk.Event):
    step_over(gd)

window.bind("<Right>", arrow_right)

window.mainloop()



# widgets:
# - Label
# - Button
# - Entry
# - Text
# - Frame

# Colour cycle: red, pink, blue, yellow, green, orange