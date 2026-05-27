# 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/
# Approach: HashMap — har sonni ko'rganda, uning juftini map'da qidiramiz
# Time: O(n) | Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index

        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index