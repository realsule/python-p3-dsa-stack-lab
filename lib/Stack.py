class Stack:

    def __init__(self, items=None, limit=100):
        self.items = list(items) if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            return
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        if target not in self.items:
         return -1

    # Reverse list so top becomes index 0, then return index directly
        return self.items[::-1].index(target)