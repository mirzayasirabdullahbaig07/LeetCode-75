class Solution:
    def rightSideView(self, root):
        ans = []

        def dfs(node, level):
            if not node:
                return
            
            # If visiting this level for the first time → add node
            if level == len(ans):
                ans.append(node.val)

            # Visit right first (this ensures rightmost node appears first)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        
        return ans
