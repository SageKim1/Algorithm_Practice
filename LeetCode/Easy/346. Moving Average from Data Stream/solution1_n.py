# Approach 1: Array or List
# Time Complexity: O(n) | n: the size of the moving window
# Space Complexity: O(m)
# m: the length of the queue which would grow at each invocation of the next(val) function
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
