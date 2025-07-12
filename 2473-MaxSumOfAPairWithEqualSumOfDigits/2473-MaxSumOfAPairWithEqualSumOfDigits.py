# Last updated: 7/12/2025, 11:46:20 PM
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        max_digit_sum_arr = [0] * 82
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            if max_digit_sum_arr[digit_sum] != 0:
                res = max(max_digit_sum_arr[digit_sum] + num, res)
            max_digit_sum_arr[digit_sum] = max(num, max_digit_sum_arr[digit_sum])

        return res