# Last updated: 8/1/2025, 11:34:47 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows -1):
            temp_arr = [0] + res[-1] + [0]
            new_arr = []
            for j in range(len(res[-1]) + 1):
                new_arr.append(temp_arr[j] + temp_arr[j + 1])
            
            res.append(new_arr)
        return res