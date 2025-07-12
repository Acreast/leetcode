# Last updated: 7/12/2025, 11:48:29 PM
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        def generate_valid_rows(m):
            result = []

            def backtrack(pos, path):
                if pos == m:
                    result.append(tuple(path))
                    return
                for color in range(3):
                    if pos == 0 or path[-1] != color:
                        path.append(color)
                        backtrack(pos + 1, path)
                        path.pop()

            backtrack(0, [])
            return result

        valid_rows = generate_valid_rows(m)
        row_count = len(valid_rows)

        transitions = {row: [] for row in valid_rows}
        for i in range(row_count):
            for j in range(row_count):
                row1, row2 = valid_rows[i], valid_rows[j]
                if all(a != b for a, b in zip(row1, row2)):
                    transitions[row1].append(row2)

        dp = {row: 1 for row in valid_rows}

        for _ in range(n - 1):
            new_dp = {row: 0 for row in valid_rows}
            for row in valid_rows:
                for next_row in transitions[row]:
                    new_dp[next_row] = (new_dp[next_row] + dp[row]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD
