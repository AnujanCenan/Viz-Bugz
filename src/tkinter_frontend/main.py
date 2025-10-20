import os
import tkinter as tk        # normal
import tkinter.ttk as ttk   # themed
from tkinter import filedialog

from constants import *
from Memory_Object import Memory_Object
from Grid_Drawing import Grid_Drawing

from LLDB_Interaction import *

import posix_ipc
from Generate_Message import *
from multiprocessing import shared_memory


sem = posix_ipc.Semaphore(SEMAPHORE_NAME)
shm = shared_memory.SharedMemory(SHARED_MEMORY_REGION_NAME, create=False)     # default to false

def send_message(message: str):
    sem.acquire()
    encoded = message.encode('utf-8')
    shm.buf[:len(encoded)] = encoded
    sem.release()

def read_message():
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
gd = Grid_Drawing(memory_grid)
gd.create_grid()
gd.label_memory_grid()
memory_grid.pack(side="left", padx=50)

mem_object = Memory_Object("x", "int", 3, 4, 42343123, 5)

next_memory = 92
next_memory = gd.add_memory_object(mem_object, next_memory, "red")


#### File selection - for selecting the current working directory
def select_file():
    print(f"PWD = {os.getcwd()}")       # gets cwd from **where** the python program was launched from
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
    step_over(gd)

window.bind("<Right>", arrow_right)

window.mainloop()


while (True):
    # sem.acquire()

    next_event = 0

    match next_event:
        case 0:
            pass
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        

    # sem.release()
    
    input_mes = "Q"
    if (input_mes == "Q"): break



# widgets:
# - Label
# - Button
# - Entry
# - Text
# - Frame

# Colour cycle: red, pink, blue, yellow, green, orange