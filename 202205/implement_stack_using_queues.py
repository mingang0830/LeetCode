from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, deque()
        return result

    def top(self) -> int:
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        result = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, deque()
        return result

    def empty(self) -> bool:
        return len(self.q1) == 0


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    print(obj.empty())
