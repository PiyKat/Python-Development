#! python3

# writing a dequeue class, note that python collections module contains dequeue object

class ArrayDequeue():

    DEFAULT_SIZE = 10

    def __init__(self):

        self._data = [None]*DEFAULT_SIZE
        self._front = 0
        self._size = 0

    def __len__(self):

        return len(self._data)

    def is_empty(self):

        return (self._size == 0)

    def pop_left(self):

        if self.is_empty:
            raise Error("No element to pop asshole")
        else:
            answer = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1)%len(self._data)
            self._size-=1

        return answer

    def pop_right(self):

        if self.is_empty:
            raise Error("No element to pop")
        else:
            back = (self._front + self._data - 1) % len(self._data)
            answer = self._data[back]
            self._data[back] = None
            self._size-=1

        return answer

    def enq_right(self,e):

        if (self._size == len(self._data)):
            self._resize(2*len(self._data))

        avail = (self._size + self._front) % len(self._data)
        self._data[avail] = e
        self._size += 1

    # A slight doubt regarding this
    
    def enq_right(self,e):

        if (self._size == len(self._data)):
            self._resize(2*len(self,_data))

        if self.front == 0:
            raise Error("Cannot add element at the front anytime")

        self._front -= 1
        self._data[self._front] = e
        self._size += 1

    def resize(self,cap):

        old = self._data
        self._data = [None]*cap

        start = self._front

        for j in range(0,cap):

            self._data[j] = old[start]
            start = (1+start)%len(start)

        return self._data


class Error(Exception):
    pass



        

        
        
            

        
        

        
        

        
            

        
            
