# Last updated: 7/12/2025, 11:52:06 PM
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        can_open = True
        total_candies = 0
        while initialBoxes and can_open:
            can_open = False
            next_boxes = []
            for box_id in initialBoxes:
                if status[box_id]:
                    can_open = True
                    next_boxes.extend(containedBoxes[box_id])
                    for key_id in keys[box_id]:
                        status[key_id] = 1
                    total_candies += candies[box_id]
                else:
                    next_boxes.append(box_id)
            initialBoxes = next_boxes

        return total_candies