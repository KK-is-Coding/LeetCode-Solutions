# Reducing Dishes

class Solution:
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort(reverse=True)
        presum, res = 0, 0
        for i in range(len(satisfaction)):
            presum += satisfaction[i]
            if presum < 0:
                continue
            res += presum
        return res
