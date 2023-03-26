# Largest Perimeter Triangle

class Solution:
    def largestPerimeter(self, nums):
        temp = 0
        peri = 0
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1]+nums[i+2] and nums[i+1] < nums[i]+nums[i+2] and nums[i+2] < nums[i]+nums[i+1]:
                temp = nums[i]+nums[i+1]+nums[i+2]
            if temp >= peri:
                peri = temp

        return peri


nums = list(map(int, input().split(" ")))
sol = Solution
out = sol.largestPerimeter(sol, nums)
print(out)
