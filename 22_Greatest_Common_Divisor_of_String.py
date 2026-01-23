class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If concatenations don't match, no common divisor string exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute GCD of the two lengths
        from math import gcd
        length = gcd(len(str1), len(str2))
        
        # The GCD string is the prefix of that length
        return str1[:length]
