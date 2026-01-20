class Solution:
    def __init__(self):
        # Phone keypad mapping - same as traditional phone buttons
        self.digits_to_letters = {
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def helper(self, digits, ans, index, current):
        # Base case: processed all digits, we have a complete combination
        if index == len(digits):
            ans.append(current)  # Add the complete combination to results
            return

        # Get all possible letters for the current digit
        letters = self.digits_to_letters.get(digits[index], "")
        
        # Try each possible letter for this digit position
        for letter in letters:
            # Recursive call: move to next digit, extend current combination
            self.helper(digits, ans, index + 1, current + letter)

    def letterCombinations(self, digits):
        ans = []
        # Handle edge case: empty input
        if not digits:
            return ans
        
        # Start the backtracking process
        self.helper(digits, ans, 0, "")  # index=0, current=""
        return ans