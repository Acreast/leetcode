# Last updated: 7/12/2025, 11:48:51 PM
class FindSumPairs:
    arr1 = []
    arr2 = []
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.arr1 = nums1
        self.arr2 = nums2
        self.counter2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        prev_val = self.arr2[index]
        new_val = prev_val + val
        self.arr2[index] = new_val

        self.counter2[prev_val] -= 1
        if self.counter2[prev_val] == 0:
            del self.counter2[prev_val]
        self.counter2[new_val] += 1


    def count(self, tot: int) -> int:
        res = 0
        for num in self.arr1:
            target = tot  - num
            res += self.counter2.get(target, 0)
        return res
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)