# Last updated: 5/1/2025, 11:51:42 PM
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can_assign(k: int) -> bool:
            dq = deque(workers[-k:])  # k strongest workers
            used = 0

            for task in reversed(tasks[:k]):  # k hardest tasks
                if dq and dq[-1] >= task:
                    dq.pop()
                else:
                    if used == pills:
                        return False
                    # Use pill on weakest worker who can do task with strength
                    idx = bisect.bisect_left(dq, task - strength)
                    if idx == len(dq):
                        return False
                    dq.remove(dq[idx])  # remove that worker
                    used += 1
            return True

        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (left + right + 1) // 2
            if can_assign(mid):
                left = mid
            else:
                right = mid - 1

        return left