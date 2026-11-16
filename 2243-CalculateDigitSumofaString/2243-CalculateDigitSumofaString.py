# Last updated: 11/16/2026, 11:54:37 PM
1class Solution:
2    def digitSum(self, s: str, k: int) -> str:
3        res = ""
4        
5        round_str = s
6        while len(round_str) > k:
7            round_arr = []
8            # Step 1 & 2: Slice into chunks of size k and calculate digit sums
9            for i in range(0, len(round_str), k):
10                group = round_str[i:i + k]
11                digit_sum = sum(int(digit) for digit in group)
12                round_arr.append(digit_sum)
13            
14            # Step 3: Join the sums back into a new string for the next round
15            round_str = "".join(str(num) for num in round_arr)
16        return round_str
17
18                
19
20
21
22                    
23            
24
25