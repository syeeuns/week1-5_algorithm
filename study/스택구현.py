class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    # 생성자
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self):
        return self.ptr

    def is_empty(self):
        return self.ptr <= 0

    def is_full(self):
        return self.ptr >= self.capacity

    def push(self, value):
        if self.is_full():
            raise FixedStack.Full

        self.stack[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty

        self.ptr -= 1
        return self.stack[self.ptr]

    def peek(self):
        if self.is_empty():
            raise FixedStack.Empty

        return self.stack[self.ptr - 1]

    def clear(self):
        self.ptr = 0

    def find(self, value):
        for i in range(self.ptr-1, -1, -1):
            if self.stack[i] == value:
                return i
        return -1

    def count(self, value):
        for i in range(self.ptr-1, -1, -1):
            if self.stack[i] == value:
                return i

    def __contains__(self, value):
        return self.count(value)

    def dump(self):
        if self.is_empty():
            print('스택이 비어 있습니다')
        else:
            print(self.stack[:self.ptr])


stack = FixedStack(5)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())