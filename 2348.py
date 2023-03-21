# Number of Zero-filled Subarrays

class Solution:
    def zeroFilledSubarray(self, nums):
        res = 0
        for i in range(len(nums)):
            flag = 0
            if nums[i] != 0:
                continue
            for j in range(len(nums)):
                if nums[i+j] == 0:
                    flag += 1
                    res += flag

        return res
