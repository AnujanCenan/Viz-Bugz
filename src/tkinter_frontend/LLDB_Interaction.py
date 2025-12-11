'''
Trigger front end actions *after* C++ backend has completed an associated action
'''

from grid_drawing import GridDrawing
def step_over(gd: GridDrawing):
    '''
    Reflects the actions of stepping over an line of code in the debugging target
    '''
    print("Stepping Over now...")
    # Obtain new line number
    # update highligted code
    # find newly created variables
    gd.draw_memory_slab(673, 679, "green")
