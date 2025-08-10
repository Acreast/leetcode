# Last updated: 8/10/2025, 6:55:07 PM
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def generate_numbers(n):
            digits = str(n)
            seen = set()

            for perm in permutations(digits):
                if perm[0] != '0':  # no leading zero
                    num = int(''.join(perm))
                    seen.add(num)

            return sorted(seen)
        

        num_set = generate_numbers(n)
        for num in num_set:
            if num > 0 and not (num & (num - 1)):
                return True
            
        
        return False