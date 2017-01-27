#! python3

class PositionalList(_DoubleLL):

    class Position:

        def __init__(self,container,node):   # What's a container

            self._container = container
            self._node = node

        def element(self):

            return self._node._element

        def __eq__(self,other):

            return self._node is other._node and type(self) is type(other)

        def __ne__(self,other):

            return not(self == other)
    

    def _validate(self,p):

        if not isinstance(p,self.Position):
            raise TypeError("p must be proper type!!")
        
        if p._container is not self:
            raise ValueError("p does not belong to this container")

        if p._node._next is None:
            raise ValueError("p is not valid anymore")

        return p._node

    def _make_position(self,node):

        if node is self._trailer or node is self._header:
            return None
        else:
            return self.Position(self,node)

    # Note - This will return the position of the first element, NOT the element
    def first(self):

        return self._make_position(self._header._next)

    def last(self):

        return self._make_position(self._trailer._prev)

    def before(self,p):

        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self,p):

        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):

        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self,e,predacessor,successor):

        node = super()._insert_between(e,predacessor,successor)
        return self._make_position(node)

    def _add_first(self,e):

        return self._insert_between(e,self._header,self._header._next)

    def _add_last(self,e):

        return self._insert_between(e,self._trailer._prev,self._trailer)

    def _add_after(self,p,e):

        valid = self._validate(p)
        return self._insert_between(e,valid,valid._next)

    def _add_before(self,p,e):

        valid = self._validate(p)
        return self._insert_between(e,valid._prev,valid)

    def delete(self,p):

        valid = self._validate(p)
        return self._delete_node(valid)

    def replace(self,p,e):

        valid = self._validate(p)
        if valid:
            if valid.element() == e:
                return "The element is the same"
            else:
                old = valid.element()
                valid._element = r

        return old
    
                

    
        
    

    

        
