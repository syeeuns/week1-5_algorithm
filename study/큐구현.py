class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity):
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.queue = [None] * capacity

    def __len__(self):
        return self.no

    def is_empty(self):
        return self.no <= 0

    def is_full(self):
        return self.no >= self.capacity

    def enque(self, value):
        if self.is_full():
            raise FixedQueue.Full

        self.queue[self.rear] = value
        self.rear += 1
        self.no += 1
        # 링 버퍼에서 rear 값이 큐의 크기까지 갔으면, 0으로 보내줘야 다음에 똑바로 넣을 수 있음
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self):
        if self.is_empty():
            raise FixedQueue.Empty

        value = self.queue[self.front]
        self.front += 1
        self.no -= 1

        # 링 버퍼에서 front 값이 큐의 크기까지 갔으면, 0으로 보내줘야 다음에 똑바로 읽을 수 있음
        if self.front == self.capacity:
            self.front = 0

        return value

    def peek(self):
        if self.is_empty():
            raise FixedQueue.Empty

        return self.queue[self.front]

    def find(self, value):
        for i in range(self.no):
            if self.queue[(i + self.front) % self.capacity] == value:
                return (i + self.front) % self.capacity
        return -1

    def count(self, value):
        c = 0
        for i in range(self.no):
            if self.queue[(i + self.front) % self.capacity] == value:
                c += 1
        return c

    def __contains__(self, value):
        return self.count(value)

    def clear(self):
        self.no = self.front = self.rear = 0

    def dump(self):
        if self.no == 0:
            print('큐가 비어 있습니다.')
        else:
            for i in range(self.no):
                print(self.queue[(i + self.front) % self.capacity], end=' ')
            print()

queue = FixedQueue(5)
queue.enque(1)
queue.enque(2)
queue.enque(3)
print(queue.deque())
print(queue.deque())
print(queue.deque())

