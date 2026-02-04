from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')   # smallest number so far
        second = float('inf')  # second smallest number so far

        for num in nums:
            if num <= first:
                first = num  # update the smallest
            elif num <= second:
                second = num  # update the second smallest
            else:
                # If we find a number bigger than both `first` and `second`, return True
                return True

        return False  # No increasing triplet found
