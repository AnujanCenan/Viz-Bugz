import tkinter as tk        # normal
import tkinter.ttk as ttk   # themed
from typing import Final    # for marking constants


MEMORY_GRID_HEIGHT: Final = 800
MEMORY_GRID_WIDTH: Final = 1000
MEMORY_GRID_SIDE_LENGTH: Final = 25

NUM_ROWS: Final = MEMORY_GRID_HEIGHT // MEMORY_GRID_SIDE_LENGTH
NUM_COLS: Final = MEMORY_GRID_WIDTH // MEMORY_GRID_SIDE_LENGTH

WORD_SIZE: Final = 8

class Memory_Object:
    def __init__(self, name: str, type: str, value: str, size: int, address: int, declaration_line: int):
        self._name = name
        self._type = type
        self._value = value
        self._size = size
        self._address = address
        self._declaration_line = declaration_line
        self._canvas_address = None

    def get_name(self):
        return self._name
    
    def get_type(self):
        return self._type
    
    def get_value(self):
        return self._value
    
    def get_size(self):
        return self._size
    
    def get_address(self):
        return self._address
    
    def get_declaration_line(self):
        return self._declaration_line
    
    def get_canvas_address(self):
        return self._canvas_address

    def set_canvas_address(self, new_canvas_address):
        self._canvas_address = new_canvas_address

    

# Gets top left corner coordinates for a grid cell at row r and column c
# relative to the top left corner of the canvas
def get_cell_coords(r: int, c: int):
    # check boundary conditions
    if (r < 0):
        raise "Cannot let number of rows be less than 0"
    if (c < 0):
        raise "Cannot let number of columns be less than 0"
    if (r >= NUM_ROWS):
        raise "Number of rows is too large for the given canvas"
    if (c >= NUM_COLS):
        raise "Number of cols is too large for the given canvas"

    return (c * MEMORY_GRID_SIDE_LENGTH, r * MEMORY_GRID_SIDE_LENGTH)

def create_grid(canvas: tk.Canvas):
    # horizontal lines
    for y in range(0, MEMORY_GRID_HEIGHT, MEMORY_GRID_SIDE_LENGTH):
        canvas.create_line(0, y, MEMORY_GRID_WIDTH, y)
    
    # vertical lines
    thickness = 0
    for x in range(0, MEMORY_GRID_WIDTH, MEMORY_GRID_SIDE_LENGTH):
        if x % WORD_SIZE == 0:
            thickness = 6
        else:
            thickness = 2
        canvas.create_line(x, 0, x, MEMORY_GRID_HEIGHT, width=thickness)


def label_memory_grid(canvas: tk.Canvas, start: int=0):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            x, y = get_cell_coords(row, col)
            x += MEMORY_GRID_SIDE_LENGTH * 0.5
            y += MEMORY_GRID_SIDE_LENGTH * 0.5

            canvas.create_text(x, y, text=f"{(row * NUM_COLS + col) + start}", font=("Arial", 6), fill="blue")

# gets the row and column of a particular grid cell
def get_row_and_col_from_cell(cell_num: int):
    row = cell_num // NUM_COLS
    col = cell_num % NUM_COLS

    return (row, col)

def draw_memory_slab(canvas: tk.Canvas, start: int, end: int, colour: str):
    r, c = get_row_and_col_from_cell(start)
    x1, y1 = get_cell_coords(r, c)

    r, c = get_row_and_col_from_cell(end)
    x3, y3 = get_cell_coords(r, c)
    x4, y4 = x3 + MEMORY_GRID_SIDE_LENGTH, y3 + MEMORY_GRID_SIDE_LENGTH

    canvas.create_rectangle(x1, y1, x4, y4, fill=colour, width=0)


# draws a rectangle around chosen cells, writing information in the rectangle
# regarding the memory object (e.g. name, value, type)
def add_memory_object(canvas: tk.Canvas, mem_obj: Memory_Object, next_memory, colour: str):
    UPPER_LIMIT = NUM_COLS * NUM_ROWS - 1
    start = next_memory
    start_row, start_col = get_row_and_col_from_cell(start)
    last_cell_in_row = (start_row + 1) * NUM_COLS - 1

    end = min(next_memory + mem_obj.get_size() - 1, UPPER_LIMIT) # TODO: at some point, if the object spills over page 1, it should go onto the next page

    mid = min(end, last_cell_in_row)
    while (mid < end):
        draw_memory_slab(canvas, start, mid, colour)
        start = mid + 1
        last_cell_in_row += NUM_COLS
        mid = min(end, last_cell_in_row)
    
    draw_memory_slab(canvas, start, end, colour)


    return end + 1

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
create_grid(memory_grid)
label_memory_grid(memory_grid)
memory_grid.pack()

mem_object = Memory_Object("x", "int", 3, 4, 42343123, 5)

next_memory = 92
next_memory = add_memory_object(memory_grid, mem_object, next_memory, "red")
next_memory = add_memory_object(memory_grid, mem_object, next_memory, "pink")

next_memory = add_memory_object(memory_grid, mem_object, next_memory, "blue")

next_memory = add_memory_object(memory_grid, mem_object, next_memory, "yellow")

next_memory = add_memory_object(memory_grid, mem_object, next_memory, "green")
next_memory = add_memory_object(memory_grid, mem_object, next_memory, "orange")




window.mainloop()



# widgets:
# - Label
# - Button
# - Entry
# - Text
# - Frame

# Colour cycle: red, pink, blue, yellow, green, orange