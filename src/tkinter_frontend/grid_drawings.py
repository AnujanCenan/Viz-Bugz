'''
Handling all drawing functionality on the frontend Tkinter canvas
'''

import tkinter as tk
from constants import(NUM_COLS, NUM_ROWS, MEMORY_GRID_HEIGHT,
    MEMORY_GRID_SIDE_LENGTH, MEMORY_GRID_WIDTH, WORD_SIZE, HALF_WORD_SIZE)
from memory_objects import MemoryObject

class GridDrawing:
    '''
    Handling all drawing functionality on the frontend Tkinter canvas
    '''
    def __init__(self, canvas: tk.Canvas):
        '''
        Initialising the class by providing the tkinter canvas to draw on
        '''
        self._canvas = canvas


    def get_cell_coords(self, r: int, c: int):
        '''
        Based on the specified row and column, obtain the (x, y) coordinates (in
        pixels) to determine the location of the grid cell's top left column.
        Relative to the top left corner of the canvas
        '''
        # check boundary conditions
        if r < 0:
            print("ERROR: Cannot let number of rows be less than 0")
            return -1
        if c < 0:
            print("ERROR: Cannot let number of columns be less than 0")
            return -1
        if r >= NUM_ROWS:
            print("ERROR: Number of rows is too large for the given canvas")
            return -1
        if c >= NUM_COLS:
            print("ERROR: Number of cols is too large for the given canvas")
            return -1

        return (c * MEMORY_GRID_SIDE_LENGTH, r * MEMORY_GRID_SIDE_LENGTH)

    def create_grid(self):
        '''
        Drawing the grid on the canvas
        '''
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
        '''
        Labels each grid cell in the canvas with a number (canvas address)
        '''
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                x, y = self.get_cell_coords(row, col)
                x += MEMORY_GRID_SIDE_LENGTH * 0.5
                y += MEMORY_GRID_SIDE_LENGTH * 0.5

                self._canvas.create_text(
                    x, y, text=f"{(row * NUM_COLS + col) + start}",
                    font=("Arial", 6), fill="blue"
                )


    # gets the row and column of a particular grid cell
    def get_row_and_col_from_cell(self, cell_num: int):
        '''
        Gets the row and column numbers given a cell number (assuming top left
        is cell 0, reading top-to-bottom, going from left to right - like an 
        English book)
        '''
        row = cell_num // NUM_COLS
        col = cell_num % NUM_COLS

        return (row, col)

    def draw_memory_slab(self, start: int, end: int, colour: str):
        '''
        Draws a memory slab in the tkinter canvas based on provided start and 
        end (canvas) addresses
        '''
        if end < start:
            print("ERROR: End must be greater than or equal to start")
            return

        r, c = self.get_row_and_col_from_cell(start)
        x1, y1 = self.get_cell_coords(r, c)

        r, c = self.get_row_and_col_from_cell(end)
        x3, y3 = self.get_cell_coords(r, c)
        x4, y4 = x3 + MEMORY_GRID_SIDE_LENGTH, y3 + MEMORY_GRID_SIDE_LENGTH

        self._canvas.create_rectangle(x1, y1, x4, y4, fill=colour, width=0)

    # draws a rectangle around chosen cells, writing information in the rectangle
    # regarding the memory object (e.g. name, value, type)
    def add_memory_object(self, mem_obj: MemoryObject, next_memory, colour: str):
        '''
        Draws a memory slab in the tkinter canvas based on provided MemoryObject,
        particularly its size in bytes
        '''
        upper_limit = NUM_COLS * NUM_ROWS - 1
        start = next_memory
        start_row = self.get_row_and_col_from_cell(start)[0]
        last_cell_in_row = (start_row + 1) * NUM_COLS - 1

        end = min(next_memory + mem_obj.get_size() - 1, upper_limit)
        # at some point, if the object spills over page 1,
        # it should go onto the next page

        mid = min(end, last_cell_in_row)
        while mid < end:
            self.draw_memory_slab(start, mid, colour)
            start = mid + 1
            last_cell_in_row += NUM_COLS
            mid = min(end, last_cell_in_row)

        self.draw_memory_slab(start, end, colour)


        return end + 1
