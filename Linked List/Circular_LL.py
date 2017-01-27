#! python3

# Creating a circualar queue ADT

class CircularQueue:

    # ---------- Nested Class ---------- #

    class _Node:

        __slots__ = '_element','_next'

        def __init__(self,element,next_ptr):

            self._element = element
            self._next = next_ptr


    def __init__(self):

        self._tail = None
        self._size = 0

    def __len__(self):

        return self._size
    
    def is_empty(self):

        return (self._size == 0)

    def first(self):

        return self._tail._next._element

    def dequeue(self):

        if self.is_empty():
            raise Error("The queue is empty!")

        answer = self._tail._next
        
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = answer._next
        
        self._size -= 1

        return answer._element

    def enqueue(self,e):

        newest = self._Node(e,None)
        
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest

        self._tail = newest
        self._size += 1

    def rotate(self,n):


        for i in range(0,n):
            
            if self._size > 0 :
                
                current = self._tail._next
                
                for j in range(0,self._size-2):
                    current = current._next

                self._tail = current


    def traverse_list(self):

        element_list = []

        head = self._tail._next
        for j in range(0,self._size):
            element_list.append(head._element)
            head = head._next

        print(element_list)

cc = CircularQueue()

cc.enqueue(5)
cc.enqueue(10)
cc.enqueue(15)
cc.enqueue(20)

cc.traverse_list()

# cc.dequeue()

# cc.traverse_list()

#cc.rotate(2)

#cc.traverse_list()

## An alternate way of doing circular linked list is underway
        
            


        
        

    
