# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        current = ''

        for l in s:
            if l in current:
                idx = current.index(l)
                current = current[idx+1:] + l
            else:
                current += l
                maximum = max(maximum, len(current))

        return maximum


s = Solution()
assert s.lengthOfLongestSubstring("dvdf") == 3
assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("bbbbb") == 1
assert s.lengthOfLongestSubstring("pwwkew") == 3
