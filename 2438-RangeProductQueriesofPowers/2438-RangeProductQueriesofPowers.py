# Last updated: 8/12/2025, 12:22:00 AM
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        result = [0] * len(queries)

        # Base for 2^30 mod MOD
        BASE_2_POW_30 = (1 << 30) % MOD

        def pow_mod_from_exponent(exp):
            """Compute (2^exp) % MOD efficiently using 2^30 chunks."""
            if exp < 30:
                return 1 << exp
            q, r = divmod(exp, 30)
            big_pow = pow(BASE_2_POW_30, q, MOD)
            return big_pow * (1 << r) % MOD

        # List of exponents of set bits in n (powers of two present in n)
        bit_exponents = []
        for bit_index in range(30):
            if (n >> bit_index) & 1:
                bit_exponents.append(bit_index)

        # Prefix sum of exponents
        prefix_exp_sum = list(accumulate(bit_exponents, initial=0))

        # Answer queries
        for idx, (start, end) in enumerate(queries):
            total_exp = prefix_exp_sum[end + 1] - prefix_exp_sum[start]
            result[idx] = pow_mod_from_exponent(total_exp)

        return result
