# Last updated: 7/12/2025, 11:47:11 PM
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)

        max_heap = [(-ord(c), cnt) for c, cnt in count.items()]
        heapq.heapify(max_heap)
        res = []

        while max_heap:
            cur_char, cur_count = heapq.heappop(max_heap)
            min_appended_count = min(repeatLimit, cur_count)
            cur_char = chr(-cur_char)
            res.append(cur_char * min_appended_count)

            if cur_count - min_appended_count > 0 and max_heap:
                next_char, next_count = heapq.heappop(max_heap)
                next_char = chr(-next_char)
                res.append(next_char)
                if next_count > 1:
                    heapq.heappush(max_heap, (-ord(next_char), next_count -1))
                heapq.heappush(max_heap, (-ord(cur_char), cur_count - min_appended_count))

        return "".join(res)
