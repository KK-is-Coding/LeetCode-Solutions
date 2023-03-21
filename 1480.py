# Running Sum of 1d Array

class Solution:
    def runningSum(self, nums):
        sum = 0
        runSum = []
        for i in nums:
            sum += i
            runSum.append(sum)

        return runSum
