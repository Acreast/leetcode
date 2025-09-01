# Last updated: 9/2/2025, 12:21:53 AM
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        heap = []
        sum = 0
        for passed, total in classes:
            sum += passed/total
            heap.append(((passed - total)/(total * (total + 1)), passed, total))
        
        heapq.heapify(heap)

        for _ in range(extraStudents):
            (avg, passed, total) = heap[0]
            if avg == 0:
                break
            sum -= avg
            new_avg = (passed - total) / ((total + 1.0) * (total + 2.0))
            heapreplace(heap, (new_avg, passed + 1, total + 1))
        return sum/len(classes)  
