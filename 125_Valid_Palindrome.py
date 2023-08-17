"""A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the 
same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise."""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_str = ""
        for i in s:  #stripping out all non-alphanumeric characters and spaces
            if i.isalnum():
                stripped_str += i.lower()
        for i in range(len(stripped_str)//2):  #iteration method, could have used stripped_str[::-1}
            if stripped_str[i] != stripped_str[-i-1]:   #to reverse string and check for equivalence
                return False
        return True
