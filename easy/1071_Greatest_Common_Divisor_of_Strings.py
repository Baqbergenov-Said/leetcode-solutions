# 1071. Greatest Common Divisor of Strings
# Difficulty: Easy
# Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Approach: If a common divisor string exists, str1+str2 == str2+str1 will hold.
#           The answer's length is the GCD (Greatest Common Divisor) of the two lengths.
# Time: O(n+m) | Space: O(n+m)

import math

def gcdOfStrings(str1: str, str2: str) -> str:
    # If a common "divisor" string exists, swapping the order of concatenation
    # must produce the same result. Otherwise, no common divisor exists.
    if str1 + str2 != str2 + str1:
        return ""
    
    # The length of the answer is the GCD of the two string lengths,
    # since the divisor string must evenly divide both strings.
    gcd = math.gcd(len(str1), len(str2))
    
    # Take the first `gcd` characters of str1 as the answer.
    return str1[:gcd]


print(gcdOfStrings(
    "CXTXNCXTXNCXTXNCXTXNCXTXN",
    "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN"
))