class Solution:
    def func(self, n, Sum, last, nums, k, ans):
        # Base case: Found valid combination
        if Sum == n and len(nums) == k:
            ans.append(list(nums))  # Make a copy to preserve state
            return
        
        # Pruning: Early termination for invalid paths
        if Sum > n or len(nums) > k:
            return

        # Try numbers from last to 9 (ascending order, no duplicates)
        for i in range(last, 10):
            nums.append(i)
            self.func(n, Sum + i, i + 1, nums, k, ans)  # Update sum and next start
            nums.pop()  # Backtrack

    def combinationSum3(self, k, n):
        ans = []
        nums = []
        self.func(n, 0, 1, nums, k, ans)  # Start with sum=0, last=1
        return ans