#! python3

import tree_abs


class BinaryTree(Tree):

    def left(self,p):

        raise NotImplementedError("Should be modified by subclass!")

    def right(self,p):

        raise NotImplementedError("Should be modified by subclass!")

    def sibling(self,p):

        parent = self.parent(p)

        if parent is None:
            return None
        elif p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self,p):

        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

        
