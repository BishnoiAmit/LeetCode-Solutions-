"""
PROBLEM: 4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
"""
Created on Wed Aug 22 16:40:42 2018

@author: bishnoiamit
"""

import math as m

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tlist = []
        pos1 = 0
        pos2 = 0
        
        while(nums1 and nums2):
            if nums1[pos1] > nums2[pos2]:
                tlist.append(nums2.pop(pos2))
            else:
                tlist.append(nums1.pop(pos1))
        
        if len(nums1)>0:
            for i in range(len(nums1)):
                tlist.append(nums1[i])
        else:
            for i in range(len(nums2)):
                tlist.append(nums2[i])
                
        if(len(tlist)%2==0):
            return ((tlist[int(len(tlist)/2)] + tlist[int(len(tlist)/2 -1)])/2)
        else:
            return (tlist[m.floor(len(tlist)/2)])

def main():
    obj = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    
    print(obj.findMedianSortedArrays(nums1, nums2))
    
main()