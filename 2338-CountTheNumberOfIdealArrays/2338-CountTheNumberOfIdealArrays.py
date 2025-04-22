# The problem is solved using combinatorics and dynamic programming.
# The approach relies on understanding how many ways a number can be 
# constructed using its prime factors and placing them in sequences of a given length.
class Solution:
    def idealArrays(self, array_length: int, max_value: int) -> int:
        from collections import defaultdict
        from functools import lru_cache

        MOD = 10 ** 9 + 7

        # Generate all prime numbers up to a limit using the Sieve of Eratosthenes
        def generate_primes(limit):
            is_prime = [True] * (limit + 1)
            primes = []
            for num in range(2, limit + 1):
                if is_prime[num]:
                    primes.append(num)
                    # Mark multiples of current prime as non-prime
                    for multiple in range(num * num, limit + 1, num):
                        is_prime[multiple] = False
            return primes
        
        # Build a map from every integer up to `limit` to its prime factor exponents
        def build_factor_map(prime_list, limit):
            factor_map = defaultdict(list)
            prime_count = len(prime_list)

            # Initialize map for each prime itself (e.g., 2 = [1, 0, 0...])
            for index, prime in enumerate(prime_list):
                factor_map[prime] = [0] * prime_count
                factor_map[prime][index] = 1

            # Fill in prime factor exponents for all numbers from 3 to limit
            for value in range(3, limit + 1):
                if value not in factor_map:
                    factor_map[value] = [0] * prime_count
                    for index, prime in enumerate(prime_list):
                        if value % prime == 0:
                            # Value is divisible by this prime
                            # Copy the factor list of value // prime and increment this prime's count
                            factor_map[value] = factor_map[value // prime].copy()
                            factor_map[value][index] += 1
                            break
            return factor_map
        @lru_cache(None)    
        # Compute combinations C(x, y) = x choose y using memoization to speed up
        def calculate_combinations(x, y):
            if y == 0:
                return 1
            if y == 1:
                return x
            if y > x:
                return 0
            # Classic Pascal's triangle recurrence
            return (calculate_combinations(x - 1, y) + calculate_combinations(x - 1, y - 1)) % MOD

        # Step 1: Generate all primes up to max_value
        primes = generate_primes(max_value)

        # Step 2: Create a map of each number up to max_value -> its prime exponent list
        factor_map = build_factor_map(primes, max_value)

        # Step 3: Total number of valid (ideal) arrays
        total_arrays = 0

        # Iterate through all possible ending values of the array
        for value in range(1, max_value + 1):
            factors = factor_map[value]  # Get prime exponents for this number
            combinations_product = 1

            # For each exponent of the prime factorization,
            # count how many ways we can distribute that factor across the array length
            for factor_count in factors:
                if factor_count > 0:
                    # Use the formula: C(factor_count + array_length - 1, factor_count)
                    # This is "stars and bars" to distribute the exponent among the positions
                    combinations_product *= calculate_combinations(factor_count + array_length - 1, factor_count)
                    combinations_product %= MOD

            # Add the result for this particular number
            total_arrays = (total_arrays + combinations_product) % MOD

        return total_arrays
