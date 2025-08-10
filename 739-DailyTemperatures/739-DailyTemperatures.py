# Last updated: 8/10/2025, 7:50:17 PM
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = []
        # tempIndex = 0
        # for i in range(0,len(temperatures)):
        #     countToEnd = len(temperatures) - i - 1
        #     for x in range(i,len(temperatures)):
        #         if i == len(temperatures) - 1:
        #             result.append(0)
        #             tempIndex = 0
        #             break
        #         elif temperatures[i+tempIndex] > temperatures[i]:
        #             result.append(tempIndex)
        #             tempIndex = 0
        #             break
        #         elif x == len(temperatures) - 1:
        #             result.append(0)
        #             tempIndex = 0
        #             break
        #         tempIndex = tempIndex + 1
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans