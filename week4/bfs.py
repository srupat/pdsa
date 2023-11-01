class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, v):
        self.queue.append(v)

    def dequeue(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    
    def isempty(self):
        return self.queue == []
    
    def __str__(self):
        return str(self.queue)

n = int(input("Enter the number of nodes\n"))

import numpy as np
A = np.zeros(shape=(n, n))
