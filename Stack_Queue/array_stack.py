#! python3
# creating an array stack class ADT using list datatype and adative design pattern

class ArrayStack():

    def __init__(self):

        self._data = []
        
    def is_empty(self):

        return (len(self._data) == 0)
    
    def push(self,x):

        self._data.append(x)

    def pop(self):

        if self.is_empty():
            raise Empty('Stack is empty')
        
        return self._data.pop()

    def __len__(self):

        return len(self._data)

    def top(self):

        if self.is_empty:
            raise Empty('Stack is empty')
        
        return self._data[-1]

    # Just for checking purposes
    
    def print_stack(self):

        print(self._data)

# Defining empty class

class Empty(Exception):
    pass

##s = ArrayStack()
###s.pop()
##print(s.is_empty())
##s.print_stack()

# An alternate, more efficient and realistic version of ArrayStack will be done later
