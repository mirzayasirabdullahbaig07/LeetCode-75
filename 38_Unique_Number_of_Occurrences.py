from typing import List
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dict = defaultdict(int)

        for item in arr:
            count_dict[item] += 1

        seen = set()

        for freq in count_dict.values():
            if freq in seen:
                return False
            seen.add(freq)

        return True