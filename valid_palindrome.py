# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [l for l in s.lower() if l.isalnum()]
        return s == s[::-1]
