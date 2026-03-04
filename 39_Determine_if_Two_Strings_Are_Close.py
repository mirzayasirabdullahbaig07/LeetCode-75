from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # If lengths are different, they can't be close
        if len(word1) != len(word2):
            return False
        
        # Count frequency of each character in both words
        counts1 = Counter(word1)
        counts2 = Counter(word2)
        
        # Two strings are close if they have the same set of characters
        # and the same frequency distribution (regardless of which char has which frequency)
        return (counts1.keys() == counts2.keys() and
                sorted(counts1.values()) == sorted(counts2.values()))

# Example usage
word1 = "aaabc"
word2 = "bbcaa"
solution = Solution()
print(solution.closeStrings(word1, word2))  # Output: True or False