class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       """Given two strings s and t, return true if t is an anagram of s, and false otherwise.
       An Anagram is a word or phrase formed by rearranging the letters of a different word or 
       phrase, typically using all the original letters exactly once.
       
       This isn't the most efficient way, improvements could be made by not creating
       new list objects and filling them."""
      
        string_to_list1 = []  #creating lists to use sort functionality
        string_to_list2 = []
        for i in s:
            string_to_list1.append(i)
        string_to_list1.sort()
        for i in t:
            string_to_list2.append(i)
        string_to_list2.sort()
        if string_to_list1 == string_to_list2:  #check sorted lists for equivalence
            return True
        else:
            return False
