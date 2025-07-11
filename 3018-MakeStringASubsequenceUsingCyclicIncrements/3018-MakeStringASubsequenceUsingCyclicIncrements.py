# Last updated: 7/12/2025, 11:44:10 PM
class Solution:
    def canMakeSubsequence(self, source: str, target: str) -> bool:
        targetIdx, targetLen = 0, len(target)  
        for currChar in source:
            if targetIdx < targetLen and (ord(target[targetIdx]) - ord(currChar)) % 26 < 2:
                targetIdx += 1  
        return targetIdx == targetLen