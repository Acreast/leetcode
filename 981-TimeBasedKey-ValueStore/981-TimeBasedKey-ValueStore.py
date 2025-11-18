# Last updated: 11/18/2025, 11:11:26 PM
class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        target_arr = self.time_dict[key]
        l = 0
        r = len(target_arr) - 1
        res = ""
        if not target_arr:
            return ""
        while l <= r:
            m = (l + r) // 2
            if target_arr[m][0] <= timestamp:
                res = target_arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
