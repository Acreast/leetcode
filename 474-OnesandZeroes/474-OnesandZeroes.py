# Last updated: 11/11/2025, 11:30:04 PM
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(index, m_count, n_count):
            if index == len(strs):
                return 0

            if (index, m_count, n_count) in dp:
                return dp[(index, m_count, n_count)]

            zero_count = strs[index].count("0")
            one_count = strs[index].count("1")
            dp[(index, m_count, n_count)] = dfs(index + 1, m_count, n_count)
            if zero_count <= m_count  and one_count <= n_count:
                dp[(index, m_count, n_count)] = max(
                    dp[(index, m_count, n_count)],
                    1 + dfs(index + 1, m_count - zero_count, n_count - one_count)
                )
            return dp[index, m_count, n_count]

        return dfs(0, m, n)