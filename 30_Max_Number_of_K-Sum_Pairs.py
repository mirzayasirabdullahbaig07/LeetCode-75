from collections import defaultdict

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        d = defaultdict(int)
        pairs = 0

        for num in nums:
            if d[k - num] > 0:
                pairs += 1
                d[k - num] -= 1
            else:
                d[num] += 1
        return pairs

# Example usage
nums = [1, 2, 3, 4]
k = 5

solution = Solution()
result = solution.maxOperations(nums, k)
print(result)  # Output: 2
