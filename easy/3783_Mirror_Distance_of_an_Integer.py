# 3120. Count the Number of Special Characters I
# Difficulty: Easy
# Link: https://leetcode.com/problems/count-the-number-of-special-characters-i/
# Approach: Collect unique uppercase letters, check if lowercase version exists
# Time: O(n) | Space: O(1) — at most 26 letters

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        unique_chars = set(word)
        special_count = 0

        for char in unique_chars:
            if char.isupper() and char.lower() in unique_chars:
                special_count += 1

        return special_count