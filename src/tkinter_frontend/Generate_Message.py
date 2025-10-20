# Python message structure:
# 2 definitive bytes

# Byte 1: flag byte - set to '1' to indicate that python interacted 
# with the shared memory last

# Byte 2: command byte - set ot some character that corresponds to 
# a particular command

# Byte 3 - Byte n: data bytes - any additional bytes used for data for
# C++ to read (e.g. a filename)

# Final Byte: Null Terminator - makes it easier for C++ to read the string till
# the intended end

def step_next_message():
    return "1N\0"

def step_in_message():
    return "1I\0"

def step_out_message():
    return "1O\0"

def quit_message():
    return "1Q\0"

def src_code_message(file: str):
    return "1F" + file + '\0'

def add_breakpoint(line_num: str):
    return "1B" + line_num + '\0'

def remove_breakpoint_message(line_num: str):
    return "1R" + line_num + '\0'

def set_project_dir_message(dir: str):
    return "1D" + dir + '\0'

