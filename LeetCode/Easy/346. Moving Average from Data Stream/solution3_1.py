# Approach 3: Circular Queue with Array
# Time Complexity: O(1)
# Space Complexity: O(n) | n: the size of the circular queue
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
