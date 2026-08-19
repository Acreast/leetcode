# Last updated: 8/20/2026, 12:27:20 AM
1class Solution:
2    def maxNumberOfFamilies(self, n, reservedSeats):
3
4        reservedSeats.sort()
5
6        m = len(reservedSeats)
7
8        reserved = [False] * 11
9
10        ans = 0
11        l = 0
12        r = 0
13        prev = 0
14
15        def check(left, right):
16            for seat in range(left, right + 1):
17                if reserved[seat]:
18                    return False
19            return True
20
21        while r < m:
22
23            # Count completely empty rows
24            ans += 2 * (reservedSeats[r][0] - prev - 1)
25
26            prev = reservedSeats[r][0]
27
28            # Mark all reserved seats in the current row
29            while r < m and reservedSeats[r][0] == reservedSeats[l][0]:
30                reserved[reservedSeats[r][1]] = True
31                r += 1
32
33            two_to_five = check(2, 5)
34            four_to_seven = check(4, 7)
35            six_to_nine = check(6, 9)
36
37            if two_to_five and six_to_nine:
38                ans += 2
39            elif two_to_five or four_to_seven or six_to_nine:
40                ans += 1
41
42            l = r
43
44            # Reset for the next row
45            reserved = [False] * 11
46
47        # Remaining rows are completely empty
48        ans += 2 * (n - prev)
49
50        return ans