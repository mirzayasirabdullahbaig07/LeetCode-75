class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1

        t0, t1, t2 = 0, 1, 1
        for i in range(3, n + 1):
            tn = t0 + t1 + t2
            t0, t1, t2 = t1, t2, tn

        return tn


n = 6
t0 = 1; t1 = 2; t2 = 4
i = 5
tn = 4

# seq = [0, 1, 1]