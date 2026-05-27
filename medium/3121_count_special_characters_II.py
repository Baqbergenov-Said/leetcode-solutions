# 3121. Count the Number of Special Characters II
# Difficulty: Medium
# Link: https://leetcode.com/problems/count-the-number-of-special-characters-ii/
#
# Approach:
#   - Track the LAST index of each lowercase letter
#   - Track the FIRST index of each uppercase letter
#   - If last lowercase comes before first uppercase → special character
#
# Time Complexity:  O(n)
# Space Complexity: O(1) — at most 26 letters

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lowercase = {}
        first_uppercase = {}

        for index, char in enumerate(word):
            if char.islower():
                last_lowercase[char] = index          # keep updating → last position
            elif char.isupper():
                if char not in first_uppercase:
                    first_uppercase[char] = index     # only save first position

        special_count = 0

        for lower_char in last_lowercase:
            upper_char = lower_char.upper()

            if upper_char in first_uppercase:
                if last_lowercase[lower_char] < first_uppercase[upper_char]:
                    special_count += 1

        return special_count