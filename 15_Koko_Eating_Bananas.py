class Solution:
    def totalHours(self, piles, hourly_rate):
        total = 0
        for i in range(len(piles)):
            total = total + math.ceil(piles[i] / hourly_rate)  # Calculate hours for each pile
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            total_hours = self.totalHours(piles, mid)
            if total_hours <= h:
                ans = mid                  # Try to find a smaller valid speed
                high = mid - 1
            else:
                low = mid + 1              # Need a higher speed
        return ans