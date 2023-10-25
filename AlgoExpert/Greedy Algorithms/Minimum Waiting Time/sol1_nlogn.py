# O(n logn) time | O(1) space
# n: the number of queries
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort() # O(n logn) time

    totalWaitingTime = 0
    for idx, duration in enumerate(queries): # O(n) time
        queriesLeft = len(queries) - (idx + 1)
        totalWaitingTime += duration * queriesLeft
    
    return totalWaitingTime
