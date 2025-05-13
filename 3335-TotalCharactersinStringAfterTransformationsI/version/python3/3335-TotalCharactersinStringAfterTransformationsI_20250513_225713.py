# Last updated: 5/13/2025, 10:57:13 PM
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7

        # dp[i]: how many characters the i-th character ('a'+i) becomes after k transformations
        dp = [1] * 26  # At t = 0

        for _ in range(t):
            new_dp = [0] * 26
            for i in range(26):
                if i == 25:  # 'z'
                    new_dp[i] = (dp[0] + dp[1]) % MOD  # 'z' -> 'a' and 'b'
                else:
                    new_dp[i] = dp[i + 1] % MOD  # c -> next letter
            dp = new_dp

        # Compute the total size
        result = 0
        for c in s:
            result = (result + dp[ord(c) - ord('a')]) % MOD

        return result
