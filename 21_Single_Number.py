class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        # XOR all numbers in the array
        for i in range(0, len(nums)):
            ans = ans ^ nums[i]
        return ans