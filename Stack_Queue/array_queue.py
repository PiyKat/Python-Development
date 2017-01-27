#! python3

# Creating a circular queue

def ArrayQueue():

    DEFAULT_SIZE = 10

    def __init__(self):

        self._data = [None]*DEFAULT_SIZE
        self._size = 0
        self._front = 0

    def __len__(self):

        return len(self._data)

    def is_empty(self):

        return self._data == 0

    def first(self):

        if self.is_empty():
            raise Empty("The queue is empty")
        else:
            return self._first
        
    def dequeue(self):

        if self.is_empty():
            raise Empty("The queue is empty")
        else:
            answer = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front+1)%len(self._data)
            self._size -= 1

        return answer

    # This is used in case the array is full and we'd like to add another element to dequeue

    def resize(self,cap):

        old = self._data
        self._data = [None]*cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1)/len(old)
        self._front = 0

    def enqueue(self,e):

        if(self._size == len(self._data)):
            self._resize(2*len(self._data))

        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1


            

        
            
        

        
        
        
        

        
