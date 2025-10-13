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
