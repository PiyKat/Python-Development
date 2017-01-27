#! python3

# Queue using Linked List

class Queue_LL:

    # -------------- Nested class for node creation ---------#

    class _Node:

        __slots__ = '_element','_next' # NOTE - slots used to streamline memory allocation by mentioning new methods/attributes that need to be created

        def __init__(self,element,next_ptr):

            self._element = element
            self._next = next_ptr


    def __init__(self):

        self._head  = None
        self._tail = None
        self._size  = 0

    def __len__(self):

        return self._size

    def is_empty(self):

        return self._size == 0

    def first(self):

        if self.is_empty():
            raise Error("The queue is empty")
        else:
            return self._head._element

    def last(self):

        if self.is_empty():
            raise Error("The queue is empty")
        else:
            return self._tail._element

    def dequeue(self):

        if self.is_empty():
            raise Error("Can't dequeue")

        answer = self._head
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return answer
    
    def enqueue(self,e):        

        
        new = self._Node(e,None)

        # Note -  for the irst enqueue, head and tail elements will be same
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new

        self._tail = new

        self._size += 1

class Error(Exception):
    pass
            

queue = Queue_LL()
print(queue.is_empty())
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)
print(queue.first())
print(queue.last())
print("Size: ", queue._size)
print(queue.dequeue())
print(queue.dequeue())
print("First Now: ",queue.first())

    
        
        

        
        

        
