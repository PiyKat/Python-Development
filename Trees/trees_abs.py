#! python3

## Creating an abstract base tree class

class Tree:

    class Position:

        def element(self):
            raise NotImplementedError("Must be implemented by inherited class")

        def __eq__(self,other):
            raise NotImplementedError("Must be implemented by inherited class")

        def __ne__(self,other):
            return not(self == other)


    def root(self,p):
        raise NotImplementedError("Must be implemented by inherited class")

    def parent(self,p):
        raise NotImplementedError("Must be implemented by inherited class")

    def num_children(self,p):
        raise NotImplementedError("Must be implemented by inherited class")

    def children(self,p):
        raise NotImplementedError("Must be implemented by inherited class")

    def __len__(self):
        raise NotImplementedError("Must be implemented by inherited class")

    def is_root(self,p):
        return self.root() == p

    def is_leaf(self,p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    ## The below runs in o(n) worst case time
    
    def depth(self,p):

        if self.root == p :
            return 0
        else:
            
            return 1 + self.depth(self.parent(p))

    ## O(n^2) implementation

    def _height1(self):

        return max([self.depth(p) for p in self.positions() if self.is_leaf(p)]) 
    
    ## o(n) implementation
    
    def _height2(self,p):

        if self.is_leaf:
            return 0
        else:
            return 1 + max(self.height2(c) for c in self.children(p))

    # For general implementation
    def height(self,p = None):

        if p == None:
            p = self.root()

        return self._height2(p)

    
        
        

        
