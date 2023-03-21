# Average Salary Excluding the Minimum and Maximum Salary
 
class Solution:
    def average(self, salary):
        salary.sort()
        i = 1
        sum = 0
        while (i < len(salary)-1):
            sum += salary[i]
            i += 1

        avg = sum/(len(salary)-2)
        return avg


salary = list(map(int, input().split(" ")))
sol = Solution
out = sol.average(sol, salary)
print(out)
