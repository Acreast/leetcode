# Last updated: 5/1/2025, 11:50:49 PM
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        left, right = 0, min(len(tasks), len(workers))

        while left < right:
            mid = (left + right + 1) // 2
            used_pills = 0
            availability = workers[-mid:]
            assignable = True

            for task in reversed(tasks[:mid]):
                if availability[-1] >=  task:
                    availability.pop()
                else:
                    index = bisect.bisect_left(availability, task - strength)
                    if index == len(availability) or used_pills == pills:
                        assignable = False
                        break
                    used_pills += 1
                    availability.pop(index)
            if assignable:
                left = mid
            else:
                right = mid - 1
        
        return left