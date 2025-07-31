# Last updated: 7/31/2025, 10:37:31 PM
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        cur = set()
        res = set()

        for num in arr:
            next_cur = {num}
            for prev in cur:
                next_cur.add(prev | num)
            cur = next_cur
            res.update(cur)

        return len(res)
