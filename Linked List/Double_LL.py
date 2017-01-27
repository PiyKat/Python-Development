#! python3

# Implementing a doubly linked list

class _DoubleLL:

    class _Node:

        __slots__ = '_element','_prev','_next'

        def __init__(self,element,prev_ptr,next_ptr):

            self._element = element
            self._prev = prev_ptr
            self._next = next_ptr

        def element(self):

            return self._element
        
    def __init__(self):

        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def is_empty(self):

        return self._size == 0

    def __len__(self):

        return self._size


    def _insert_between(self,e,predecessor,successor):

        newest = self._Node(e,predecessor,successor)

        predecessor._next = newest
        successor._prev = newest

##        self._header._next = newest
##        newest._next = self._trailer
##        self._trailer._prev = newest
##        newest._prev = self._header

        self._size += 1
        return newest

    def _delete_node(self,node):

        if self.is_empty():
            raise Error("Can't delete node")
        
        prev = node._prev
        trail = node._next
        prev._next = trail
        trail._prev = prev

        node._element = node._next = node._prev = None
        self._size -= 1

class Error(Exception):
    pass

