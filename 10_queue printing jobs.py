# queue printing jobs
from collections import deque

def queues():
    q = deque()
    
    def appending(document):
        q.append(document)
        
    while len(q) > 0:
        print(q.popleft())
        
    
