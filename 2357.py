# Make Array Zero by Subtracting Equal Amounts

class Solution:
    def minimumOperations(self, nums):
        counter = 0
        while sum(nums) != 0:
            nums = [i for i in nums if i != 0]
            x = min(nums)
            nums = list(map(lambda a: a-x, nums))
            counter += 1
        return counter
