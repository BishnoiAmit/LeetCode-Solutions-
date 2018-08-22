
"""
PROBLEM: 3

Given a string, find the length of the longest substring without repeating characters.
"""

"""
Created on Wed Aug 22 12:48:41 2018

@author: bishnoiamit
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """  
        tlist = []
        f_count = 0    
        
        olist = list(s)
        
        while(olist):
            elem = olist.pop(0)                
            
            if elem in tlist:
                count = len(tlist)
                if f_count < count:
                    f_count = count
                del tlist[:(tlist.index(elem))+1]
            tlist.append(elem)

            
        count = len(tlist)
        if f_count < count:
            f_count = count   
        return f_count

def main():
    obj = Solution()
    s = input("Please enter the string:")
    final_length = obj.lengthOfLongestSubstring(s)    
    print("Length of the longest substring is: %d" %final_length)


main()
