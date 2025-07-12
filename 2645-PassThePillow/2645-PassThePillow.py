# Last updated: 7/12/2025, 11:45:23 PM
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # direction = 1
        # ptr = 1
        # for i in range(time):
        #     # traverse
        #     ptr += 1 * direction
        #     if ptr == 1 or ptr == n:
        #         direction *= -1
        
        # return ptr
        chunks = time // (n - 1)
        return (time % (n - 1) + 1) if chunks % 2 == 0 else (n - time % (n - 1))
