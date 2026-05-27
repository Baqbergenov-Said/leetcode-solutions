# 9. Palindrome Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/palindrome-number/
# Approach: Convert to string and compare with its reverse
# Time: O(d) — d is number of digits | Space: O(d)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]  # negative numbers also handled automatically