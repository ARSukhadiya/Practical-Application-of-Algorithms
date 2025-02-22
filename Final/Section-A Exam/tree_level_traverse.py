# **Problem4-Leetcode#102-Binary Tree Level Order Traversal-Medium**

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# **Example 1:**
# ![tree1.jpg](attachment:896b03ec-fa75-4b76-b0de-69d3f23f255c.jpg)

# - Input: root = [3,9,20,null,null,15,7]
# - Output: [[3],[9,20],[15,7]]


from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
