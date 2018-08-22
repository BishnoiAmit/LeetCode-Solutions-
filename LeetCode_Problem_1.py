
"""
PROBLEM 1:
    
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

"""
Created on Wed Aug 22 13:03:38 2018

@author: bishnoiamit
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            diff=target - v
            for j in range(i+1, len(nums)):
                if diff==nums[j]:
                    return [i,j]
                
def main():
    obj = Solution()
    nums = [2,7,11,15]
    target = 9
    
    print(obj.twoSum(nums, target))

main()
    