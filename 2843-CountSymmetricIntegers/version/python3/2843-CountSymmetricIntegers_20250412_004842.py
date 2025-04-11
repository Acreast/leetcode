# Last updated: 4/12/2025, 12:48:42 AM
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        def is_sym(num):
            num_string = str(num)
            if len(num_string) % 2 != 0:
                return False
            mid = len(num_string) // 2
            return sum(map(int, num_string[:mid])) == sum(map(int, num_string[mid:]))
            
        count = 0
        for i in range(low, high + 1):
            count += is_sym(i)
                    
        return count