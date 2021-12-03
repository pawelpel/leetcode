# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        longest_len = 1
        s_len = len(s)
        for i in range(s_len):
            for j in range(i + longest_len, s_len):
                if s[i] != s[j]:
                    continue
                tmp = s[i:j + 1]
                if tmp == tmp[::-1]:
                    longest = tmp
                    longest_len = j + 1 - i
        return longest


s = Solution()
assert s.longestPalindrome("babad") == "bab"
assert s.longestPalindrome("cbbd") == "bb"
assert s.longestPalindrome("c") == "c"
assert s.longestPalindrome("ca") == "c"
assert s.longestPalindrome("qwertyasdfgzxcvbwweeww") == "wweeww"
