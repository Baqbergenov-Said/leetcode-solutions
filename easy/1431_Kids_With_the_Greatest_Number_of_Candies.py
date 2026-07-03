# 1431. Kids With the Greatest Number of Candies
# Difficulty: Easy
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Approach: Find the max value in candies, then check for each kid if adding
#           extraCandies makes their count >= max.
# Time: O(n) | Space: O(n)

candies = [12, 1, 12]
extraCandies = 10
max_num = max(candies)
result = []

# Har bir bola uchun, agar unga extraCandies qo'shilganda
# eng ko'p konfetga ega bo'lgan boladan kam bo'lmasa — True qo'shamiz
for i in candies:
    if max_num <= i + extraCandies:
        result.append(True)
    else:
        result.append(False)

print(result)