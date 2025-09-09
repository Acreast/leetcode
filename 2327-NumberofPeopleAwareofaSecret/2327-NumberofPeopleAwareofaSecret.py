# Last updated: 9/9/2025, 11:17:13 PM
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        if n == 1:
            return 1
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        window = 0
        for i in range(2, n + 1):
            enter = i - delay
            forgot = i - forget
            if enter >= 1:
                window = (window + dp[enter]) % MOD
            if forgot >= 1:
                window = (window - dp[forgot] + MOD) % MOD

            dp[i] = window
        start = max(1, n - forget + 1)
        res = sum(dp[start: n + 1]) % MOD
        return res