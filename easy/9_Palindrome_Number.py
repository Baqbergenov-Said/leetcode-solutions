# 3783. Mirror Distance of an Integer
# Difficulty: Easy
# Link: https://leetcode.com/problems/mirror-distance-of-an-integer/
# Approach: Reverse the number as string, convert back to int, take absolute difference
# Time: O(d) — d is number of digits | Space: O(d)

class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(str(n)[::-1]))