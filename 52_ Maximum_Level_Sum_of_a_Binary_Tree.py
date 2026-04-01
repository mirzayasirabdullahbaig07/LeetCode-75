# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import Optional

class Solution:
    def helper(self, root, level):
        if root:
            self.level[level] += root.val
            self.helper(root.left, level+1)
            self.helper(root.right, level+1)

    def maxLevelSum(self, root: Optional['TreeNode']) -> int:
        self.level = defaultdict(int)
        self.helper(root, 1)
        return sorted(self.level.items(), key=lambda x: x[1], reverse=True)[0][0]

# Example of level dictionary from the image
level = {1: 1, 2: 7, 3: -1, 4: 7}

# Example usage / test
print([[2,7], [1,1], [3,-1]])
        