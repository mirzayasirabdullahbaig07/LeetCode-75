# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = 0
        pathSums = defaultdict(int)
        pathSums[0] = 1

        def dfs(node, currSum):
            nonlocal paths

            if not node:
                return

            currSum += node.val

            # Check how many times we've seen (currSum - targetSum)
            paths += pathSums[currSum - targetSum]

            # Add current sum to hashmap
            pathSums[currSum] += 1

            # Traverse children
            dfs(node.left, currSum)
            dfs(node.right, currSum)

            # Backtrack
            pathSums[currSum] -= 1

        dfs(root, 0)
        return paths