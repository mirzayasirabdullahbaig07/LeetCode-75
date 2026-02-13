class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}

        l, cnt, res = 0, 0, 0
        for r in range(len(s)):
            cnt += 1 if s[r] in vowel else 0
            if r - l + 1 > k:
                cnt -= 1 if s[l] in vowel else 0
                l += 1
            res = max(res, cnt)
        return res