import tkinter as tk
from constants import *
from Memory_Object import Memory_Object

class Grid_Drawing:
    def __init__(self, canvas: tk.Canvas):
        self._canvas = canvas

    # Gets top left corner coordinates for a grid cell at row r and column c
    # relative to the top left corner of the canvas
    def get_cell_coords(self, r: int, c: int):
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

    def create_grid(self):
        # horizontal lines
        for y in range(0, MEMORY_GRID_HEIGHT, MEMORY_GRID_SIDE_LENGTH):
            self._canvas.create_line(0, y, MEMORY_GRID_WIDTH, y)
        
        # vertical lines
        thickness = 0
        for x in range(0, MEMORY_GRID_WIDTH, MEMORY_GRID_SIDE_LENGTH):
            line_num = x // MEMORY_GRID_SIDE_LENGTH
            if line_num % WORD_SIZE == 0:
                thickness = 6
            elif line_num % HALF_WORD_SIZE == 0:
                thickness = 4
            else:
                thickness = 2
            self._canvas.create_line(x, 0, x, MEMORY_GRID_HEIGHT, width=thickness)

    def label_memory_grid(self, start: int=0):
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                x, y = self.get_cell_coords(row, col)
                x += MEMORY_GRID_SIDE_LENGTH * 0.5
                y += MEMORY_GRID_SIDE_LENGTH * 0.5

                self._canvas.create_text(x, y, text=f"{(row * NUM_COLS + col) + start}", font=("Arial", 6), fill="blue")


    # gets the row and column of a particular grid cell
    def get_row_and_col_from_cell(self, cell_num: int):
        row = cell_num // NUM_COLS
        col = cell_num % NUM_COLS

        return (row, col)

    def draw_memory_slab(self, start: int, end: int, colour: str):
        if end < start:
            raise "End must be greater than or equal to start"
        
        r, c = self.get_row_and_col_from_cell(start)
        x1, y1 = self.get_cell_coords(r, c)

        r, c = self.get_row_and_col_from_cell(end)
        x3, y3 = self.get_cell_coords(r, c)
        x4, y4 = x3 + MEMORY_GRID_SIDE_LENGTH, y3 + MEMORY_GRID_SIDE_LENGTH

        self._canvas.create_rectangle(x1, y1, x4, y4, fill=colour, width=0)

    # draws a rectangle around chosen cells, writing information in the rectangle
    # regarding the memory object (e.g. name, value, type)
    def add_memory_object(self, mem_obj: Memory_Object, next_memory, colour: str):
        UPPER_LIMIT = NUM_COLS * NUM_ROWS - 1
        start = next_memory
        start_row, start_col = self.get_row_and_col_from_cell(start)
        last_cell_in_row = (start_row + 1) * NUM_COLS - 1

        end = min(next_memory + mem_obj.get_size() - 1, UPPER_LIMIT) # TODO: at some point, if the object spills over page 1, it should go onto the next page

        mid = min(end, last_cell_in_row)
        while (mid < end):
            self.draw_memory_slab(start, mid, colour)
            start = mid + 1
            last_cell_in_row += NUM_COLS
            mid = min(end, last_cell_in_row)
        
        self.draw_memory_slab(start, end, colour)


        return end + 1

