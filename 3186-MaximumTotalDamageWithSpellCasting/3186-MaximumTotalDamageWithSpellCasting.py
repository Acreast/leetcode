# Last updated: 10/11/2025, 7:41:38 PM
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq)
        n = len(keys)
        dp = [0] * n
        dp[0] = freq[keys[0]] * keys[0]

        for i in range(1,n):
            take = freq[keys[i]] * keys[i]
            l, r, res = 0, i - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if keys[mid] <= keys[i] - 3:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            if res >= 0:
                take += dp[res]
            
            dp[i] = max(dp[i - 1], take)
        
        return dp[-1]

            