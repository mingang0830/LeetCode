from typing import List

class MyQueue:

    def __init__(self):
        self.main_stack: List[int] = [] 
        self.sub_stack: List[int] = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)

    def pop(self) -> int:
        while self.main_stack: 
            temp1 = self.main_stack.pop() 
            self.sub_stack.append(temp1)
        
        result = self.sub_stack.pop()
        
        while self.sub_stack:
            temp2 = self.sub_stack.pop()
            self.main_stack.append(temp2)
        return result

    def peek(self) -> int:
        while self.main_stack: 
            temp1 = self.main_stack.pop() 
            self.sub_stack.append(temp1)
        
        result = self.sub_stack[-1]
        
        while self.sub_stack:
            temp2 = self.sub_stack.pop()
            self.main_stack.append(temp2)
        return result

    def empty(self) -> bool:
        return len(self.main_stack) == 0