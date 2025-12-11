'''
The Memory Object class is responsible for storing information regarding each
piece of memory (e.g. variables) in the program being debugged
'''

class MemoryInformation:
    '''
    Storing memory-specific information of a memory object in the debugging target
    '''
    def __init__(self, data_type: str, byte_size: int, value: str, mem_address: int):
        ''' 
        data_type: the type of the data stored in the associated memory object 
        byte_size: the size of the memory segment in bytes
        value: the value associated with the memory object in the program
        mem_address: the memory address of object in the original program
        '''

        self._data_type = data_type
        self._byte_size = byte_size
        self._value = value
        self._memory_address = mem_address

    def get_type(self):
        '''
        Getter for Memory Information type
        '''
        return self._data_type

    def get_value(self):
        '''
        Getter for Memory Information value
        '''
        return self._value

    def get_size(self):
        '''
        Getter for Memory Information size (in bytes)
        '''
        return self._byte_size

    def get_address(self):
        '''
        Getter for Memory Information (starting) memory address
        '''
        return self._memory_address


class MemoryObject:
    '''
    Stores all information required for a memory object from the debugging target
    '''
    def __init__(self, name: str, memory_info: MemoryInformation, declaration_line: int):
        '''
        - name: identifier name given in the program being debugged
        - memory_info: memory information associated with the memory
        - declaration_line: the line that the object was declared in
        '''

        self._name = name
        self._memory_info = memory_info
        self._declaration_line = declaration_line
        self._canvas_address = None

    def get_name(self):
        '''
        Getter for Memory Object name
        '''
        return self._name

    def get_type(self):
        '''
        Getter for Memory Object type
        '''
        return self._memory_info.get_type()

    def get_value(self):
        '''
        Getter for Memory Object value
        '''
        return self._memory_info.get_value()

    def get_size(self):
        '''
        Getter for Memory Object size (in bytes)
        '''
        return self._memory_info.get_size()

    def get_address(self):
        '''
        Getter for Memory Object (starting) memory address
        '''
        return self._memory_info.get_address()

    def get_declaration_line(self):
        '''
        Getter for Memory Object declaration line
        '''
        return self._declaration_line

    def get_canvas_address(self):
        '''
        Getter for Memory Object canvas address (in the frontend)
        '''
        return self._canvas_address

    def set_canvas_address(self, new_canvas_address):
        '''
        Setter for Memory Object canvas address (in the frontend)
        '''
        self._canvas_address = new_canvas_address
