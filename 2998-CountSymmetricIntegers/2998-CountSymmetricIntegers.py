# Last updated: 7/12/2025, 11:44:13 PM
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