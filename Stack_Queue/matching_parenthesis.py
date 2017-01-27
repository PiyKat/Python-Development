#! python3
# Checking parenthesis, runs in O(n) time

from array_stack import ArrayStack

def check_parenthesis(string):

    S = ArrayStack()
    open_par = '({['
    close_par = ')}]'
    
    for c in string:

        if c in open_par:
            S.push(c)
            
        elif c in close_par:
            
            if S.is_empty():
                return False
            
            elif close_par.index(c) != open_par.index(S.pop()):
                return False
    
    return S.is_empty()


print(check_parenthesis("({[]})"))

            

            
