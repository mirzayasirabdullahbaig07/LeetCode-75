# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        # If the root itself is the node to delete
        if root.val == key:
            return self.deletion(root)

        temp = root

        while temp is not None:
            if key < temp.val:
                if temp.left and temp.left.val == key:
                    temp.left = self.deletion(temp.left)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right and temp.right.val == key:
                    temp.right = self.deletion(temp.right)
                    break
                else:
                    temp = temp.right

        return root

    def deletion(self, node: TreeNode) -> TreeNode:
        """Delete the node based on 3 BST deletion cases."""
        # Case 1: No left child
        if node.left is None:
            return node.right

        # Case 2: No right child
        if node.right is None:
            return node.left

        # Case 3: Both children exist
        right_child = node.right
        last_right = self.findLastRight(node.left)
        last_right.right = right_child
        return node.left

    def findLastRight(self, node: TreeNode) -> TreeNode:
        """Find rightmost node in a subtree."""
        while node.right:
            node = node.right
        return node
