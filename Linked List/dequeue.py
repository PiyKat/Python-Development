#! python3
import Double_LL

class dequeue(_DoubleLL):

    def __init__(self):

        super.__init__(self)

    def first(self):

        if self.is_empty():

            raise Error("The queue is empty")
        else:
            return self._header._next._element

    def last(self):

        if self.is_empty():

            raise Error("The queue is empty")
        else:

            return self._trailer._prev._element

    def insert_first(self,e):

        self._insert_between(e,self._header,self._header._next)
        self._size += 1
        
    def insert_last(self,e):

        self._insert_between(e,self._trailer._prev,self._trailer)
        self._size -= 1

    def delete_first(self,e):

        if self.is_empty():
            raise Error("The queue is empty")
        else:
            self._delete_node(self._header._next)

        self._size -= 1

    def delete_last(self,e):

        if self.is_empty():
            raise Error("The queue is empty")
        else:
            self._delete_node(self._trailer._prev)
        
        self._size -= 1
    

    
    
