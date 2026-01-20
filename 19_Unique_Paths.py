class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the previous row with 0s
        prev = [0] * n

        for i in range(m):
            # Initialize the current row
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = 1  # Start position
                else:
                    up = prev[j] if i > 0 else 0
                    left = curr[j-1] if j > 0 else 0
                    curr[j] = up + left
            prev = curr  # Update previous row

        return prev[-1]
