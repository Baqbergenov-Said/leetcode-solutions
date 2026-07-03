
# Difficulty: Easy
# Link: https://leetcode.com/problems/can-place-flowers/
#
# Approach:
# We walk through the flowerbed from left to right, index by index.
# For each plot, we check if a new flower CAN be planted there.
# A flower can only be planted if:
#   1. The current plot is empty (0)
#   2. The plot to the LEFT is either empty (0) or doesn't exist (we're at index 0)
#   3. The plot to the RIGHT is either empty (0) or doesn't exist (we're at the last index)
#
# If all 3 conditions are true, we "plant" a flower by setting flowerbed[index] = 1.
# This is important because it updates the array in real time — so when we later
# check the NEXT index's left neighbor, it correctly sees this plot as occupied,
# preventing two flowers from ever being adjacent.
#
# We keep a counter of how many flowers we successfully planted.
# At the end, if that counter is >= n, it means we had enough room to plant
# all n flowers without breaking the no-adjacent rule, so we return True.
#
# Time: O(n)  -> we go through the flowerbed once
# Space: O(1) -> we modify the array in place, no extra data structures used

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # tracks how many flowers we've successfully planted

        for index in range(len(flowerbed)):
            # Only consider plots that are currently empty
            if flowerbed[index] == 0:

                # Check the left side: safe if we're at the very start,
                # or if the plot before us is also empty
                if index == 0 or flowerbed[index-1] == 0:

                    # Check the right side: safe if we're at the very end,
                    # or if the plot after us is also empty
                    if index == len(flowerbed)-1 or flowerbed[index+1] == 0:

                        # All conditions met — plant a flower here
                        flowerbed[index] = 1

                        # Mark this plot as occupied so future checks
                        # (the next index's "left neighbor" check) are accurate
                        count += 1

        # If we managed to plant at least n flowers, it's possible
        return count >= n