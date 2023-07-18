#Author: Isaac Johnson
#Title: Leetcode Problem 217. Contains Duplicate
#Date: 20230413

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #using set to remove duplicates then checking if length is the same
        if len(set(nums)) != len(nums):
            return True
        else:
            return False