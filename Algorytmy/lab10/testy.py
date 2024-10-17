class PriorityQueue:
    def __init__(self):
        self._queue = []

    def is_empty(self):
        return len(self._queue) == 0

    def push(self, item, priority):
        self._queue.append((item, priority))

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        min_index = 0
        for i in range(1, len(self._queue)):
            if self._queue[i][1] < self._queue[min_index][1]:
                min_index = i
        return self._queue.pop(min_index)[0]
    



q= PriorityQueue()

# Dodawanie elementów do kolejki
# queue.push("Item 1", 3)
# queue.push("Item 2", 1)
# queue.push("Item 3", 2)

# Pobieranie elementów z kolejki
# while not queue.is_empty():
#     item = queue.pop()
#     print(item)
n=9
visited=[]
for _ in range(n):
    visited.append(False)
T=[]

u=0
visited[u]=True
for i in range(n):
    pass
