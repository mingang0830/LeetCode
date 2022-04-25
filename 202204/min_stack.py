# class MinStack:
#
#     def __init__(self):
#         self.stack = []
#
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#
#     def pop(self) -> None:
#         if self.stack :
#             self.stack.pop()
#
#     def top(self) -> int:
#         if self.stack :
#             return self.stack[-1]
#
#     def getMin(self) -> int:
#         return min(self.stack)

class MinStack:

    def __init__(self):
        self.stack_ = []

    def push(self, val: int) -> None:
        if self.stack_:
            self.stack_.append((val, min(val, self.stack_[-1][1])))
        else:
            self.stack_.append((val, val))

    def pop(self) -> None:
        if self.stack_:
            self.stack_.pop()

    def top(self) -> int:
        if self.stack_:
            return self.stack_[-1][0]

    def getMin(self) -> int:
        if self.stack_:
            return self.stack_[-1][1]

    def __repr__(self):
        if self:
            return "{}".format(self.stack_)


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(-0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
