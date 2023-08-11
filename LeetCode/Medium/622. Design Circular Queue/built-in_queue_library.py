from queue import Queue

# 1. initialize a queue
q = Queue()

# 2. get the first element - return None if queue is empty
print("the first element is:", q.queue[0] if not q.empty() else None)

# 3. push new element
q.put(5)
q.put(13)
q.put(8)
q.put(6)

# 4. pop an element
q.get()

# 5. get the first element
print("the first element is:", q.queue[0] if not q.empty() else None)

# 6. get the size of the queue
print("the size is:", q.qsize())
