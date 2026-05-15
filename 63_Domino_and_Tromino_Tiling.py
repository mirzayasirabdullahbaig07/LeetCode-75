class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007

        # Handle small base cases directly
        if n <= 2:
            return n  # dp[1]=1, dp[2]=2
        if n == 0:
            return 1  # dp[0]=1 conceptually

        dp = [0] * (n + 1)

        # Initialize base cases
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        # Apply the recurrence relation
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]