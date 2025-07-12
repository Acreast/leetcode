# Last updated: 7/12/2025, 11:44:48 PM
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(i):
            for f in range(2, int(sqrt(i)) + 1):
                if i % f == 0:
                    return False
            return True

        prev = 0
        for n in nums:
            upper_bound = n - prev

            largest_prime = 0
            for i in reversed(range(2, upper_bound)):
                if is_prime(i):
                    largest_prime = i
                    break

            if n - largest_prime <= prev:
                return False
            prev = n - largest_prime

        return True