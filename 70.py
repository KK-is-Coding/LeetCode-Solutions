# Climbing Stairs

class Solution:
    def climbStairs(self, n):
        one, two = 1, 1
        for i in range(n-1):
            temp = one+two
            one = two
            two = temp
        return two
