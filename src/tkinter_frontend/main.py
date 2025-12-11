'''
Primary module responsible for hosting the (Pythong Tkinter) frontend.
'''
import os
import tkinter as tk        # normal
from tkinter import filedialog
from multiprocessing import shared_memory

import posix_ipc

from constants import (SHARED_MEMORY_REGION_NAME,
    SEMAPHORE_NAME, MEMORY_GRID_HEIGHT, MEMORY_GRID_WIDTH, NUM_ROWS, NUM_COLS,
    MAX_MESSAGE_SIZE)

from grid_drawings import GridDrawing
from lldb_interactions import step_over
from generate_messages import set_project_dir_message, quit_message



sem = posix_ipc.Semaphore(SEMAPHORE_NAME)
shm = shared_memory.SharedMemory(SHARED_MEMORY_REGION_NAME, create=False)     # default to false


def send_message(message: str):
    '''
    Sends a message via a semaphore
    '''
    sem.acquire()
    encoded = message.encode('utf-8')
    shm.buf[:len(encoded)] = encoded
    sem.release()


def read_message():
    '''
    Reads a message contained within a semaphore
    '''
    sem.acquire()
    data = shm.buf[:MAX_MESSAGE_SIZE].tobytes().decode()
    sem.release()
    return data


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
gd = GridDrawing(memory_grid)
gd.create_grid()
gd.label_memory_grid()
memory_grid.pack(side="left", padx=50)



def select_file():
    '''
    File selection - for selecting the current working directory
    '''
    print(f"PWD = {os.getcwd()}")       # gets cwd from **where**
                                        # the python program was launched from
    dir_path = filedialog.askdirectory(initialdir=os.getcwd())
    print(f"File path = {dir_path}")
    message  = set_project_dir_message(dir_path)
    print(f"Going to send message: {message}")
    send_message(message)
    return dir_path


open_button = tk.Button(window, text="Open File", command=select_file)
open_button.pack(pady=20)


### Event Handling


def arrow_right(_: tk.Event):
    '''
    Detecting a right arrow press, triggering a "step-over" debugging step
    '''
    step_over(gd)

window.bind("<Right>", arrow_right)

def close_app():
    '''
    Detects the frontend being quit, and sends the corresponding message to the
    C++ backend
    '''
    print("Quitting...")
    message = quit_message()
    send_message(message)

window.mainloop()

close_app()


# widgets:
# - Label
# - Button
# - Entry
# - Text
# - Frame

# Colour cycle: red, pink, blue, yellow, green, orange
