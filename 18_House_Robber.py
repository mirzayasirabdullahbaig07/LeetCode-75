class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        prev2 = nums[0]      # dp[i-2]
        prev1 = max(nums[0], nums[1])   # dp[i-1]

        for i in range(2, n):
            pick = nums[i] + prev2
            not_pick = prev1
            curr = max(pick, not_pick)

            prev2 = prev1
            prev1 = curr

        return prev1
