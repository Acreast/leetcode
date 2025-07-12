# Last updated: 7/12/2025, 11:51:30 PM
class Solution:
    def numSteps(self, s: str) -> int:
        def addOnes(s):
            s = list(s)
            shift_ones = False
            for i in range(len(s) -1, -1, -1):
                if s[i] == '1':
                    s[i] = '0'
                    shift_ones = True
                else:
                    s[i] = '1'
                    shift_ones = False
                    break
            if shift_ones:
                s.insert(0,'1')
            return ''.join(s)

        res = 0
        while (s != "1"):
            if (s[-1] == '0'):
                s = s[:-1]
                res += 1
            else:
                s = addOnes(s)
                res += 1

        return res