# Last updated: 9/27/2025, 9:09:38 PM
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver_arr1 = version1.split(".")
        ver_arr2 = version2.split(".")

        shorter_arr = ver_arr1 if len(ver_arr1) <= len(ver_arr2) else ver_arr2
        longer_arr = ver_arr1 if len(ver_arr1) > len(ver_arr2) else ver_arr2
        for i in range(len(shorter_arr)):
            if int(ver_arr1[i]) < int(ver_arr2[i]):
                return -1
            elif int(ver_arr1[i]) > int(ver_arr2[i]):
                return 1
        # At this point they are equal, till the same decimal place, so we check for further decimal places
        if longer_arr:
            for i in range(len(shorter_arr), len(longer_arr)):
                if int(longer_arr[i]):
                    # This means the longer array has a valid number and is hence larger.
                    if len(ver_arr1) > len(ver_arr2):
                        return 1
                    else:
                        return -1
        return 0
        




