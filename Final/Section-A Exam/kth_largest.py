# **Problem1-Leetcode#703-Kth Largest Element in a Stream-Easy**

# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

# **Example 1:**

# - Input
#     - ["KthLargest", "add", "add", "add", "add", "add"]
#     - [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# - Output
#     - [null, 4, 5, 5, 8, 8]

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
