class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0
        
        for change in gain:
            altitude += change
            max_altitude = max(max_altitude, altitude)
        
        return max_altitude
