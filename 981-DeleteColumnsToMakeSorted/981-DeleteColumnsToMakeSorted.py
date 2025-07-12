# Last updated: 7/12/2025, 11:54:02 PM
class Solution(object):
    def minDeletionSize(self, strs):
        counter = 0
        for i in range(len(strs[0])): # iterate through each column
            sorted = True
            for j in range(1, len(strs)): # iterate through each string in the column
                if strs[j][i] < strs[j-1][i]: # check if the current string is lexicographically smaller than the previous string
                    sorted = False
                    break
            if not sorted:
                counter += 1
        return counter