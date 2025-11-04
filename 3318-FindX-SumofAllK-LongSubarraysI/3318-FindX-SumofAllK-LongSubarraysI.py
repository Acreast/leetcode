# Last updated: 11/5/2025, 12:18:29 AM
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []

        for i in range(len(nums) - k + 1 ):
            count = Counter(nums[i:i+k])
            if (len(count)) <= x:
                res.append(sum(nums[i:i+k]))
            else:    
                num_list = list(count.items())
                num_list.sort(key = lambda p:(p[1], p[0]), reverse = True)
                cur_count = 0
                for num_count, num in num_list[:x]:
                    cur_count += num_count * num
                res.append(cur_count)

        return res