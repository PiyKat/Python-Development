#! python3

# creating array using linked list
class LinkedList:

    # ------------- Nested Class for Node ----------------- #
    class _Node:

        __slots__ = '_element','_next'
        
        def __init__(self,element,next_ptr):

            self._element = element
            self._next = next_ptr


    def __init__(self):

        self._head = None
        self._size = 0

    def __len__(self):

        return self._size

    def is_empty(self):

        return self._size == 0

    def push(self,e):

        self._head = self._Node(e,self._head)
        self._size += 1

    def top(self):

        if self.is_empty == 0 is True:
            raise Error("The list is empty!")

        return self._head._element

    def pop(self):

        if self.is_empty is True:
            raise Error("The list is full")
        else:
            answer = self._head
            self._head = self._head._next
            self._size -= 1

        return answer


class Error(Exception):
    pass


LL = LinkedList()
print(LL.is_empty())
LL.push(3)
LL.push(5)
LL.push(10)
LL.push(15)
x = LL.pop()
print(x._element)
print(LL.__len__())
print(LL.top())
      

    

        
        

    
