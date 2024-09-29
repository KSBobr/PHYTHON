"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/flip-string-to-monotone-increasing/?envType=problem-list-v2&envId=string
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        length = len(s)
        C1 = [0] * length
        one_count = 0

        for i in range(length):
            if s[i] == "1":
                one_count += 1
            C1[i] = one_count

        previous_value = 0
        for i in range(1, length + 1):
            if s[i - 1] == "0":
                current_value = min(previous_value + 1, C1[i - 1])
            else:
                current_value = min(previous_value, C1[i - 1])
            previous_value = current_value

        return previous_value
