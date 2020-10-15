# Created by Pooja
# On 15 Oct 2020
#Qestion :
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution:
    def solve(self,nums, start, end):
        ans = nums[start]
        dp =[0]*len(nums)
        dp[start]= nums[start]
        for i in range(start+1, end+1):
            last = dp[i-1]
            lastToLast = 0 if i-2 < start else dp[i-2]
            dp[i] = max(nums[i] + lastToLast, last)
            ans = max(dp[i], ans)
        return ans
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        return max(self.solve(nums,0,n-2),self.solve(nums,1,n-1))
    
