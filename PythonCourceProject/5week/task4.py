"""https://leetcode.com/problem-list/hash-table/
url:https://leetcode.com/problems/integer-to-roman/"""


class Solution(object):
    def intToRoman(self, num):
        ans = ""
        Dict = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        temp = 1000
        while temp >= 1:
            # print(num)
            zn = num / temp
            # print(zn)
            if zn <= 3:
                ans += zn * Dict[temp]
            elif zn <= 5:
                ans = ans + (5 - zn) * Dict[temp] + Dict[5 * temp]
            elif zn <= 8:
                # print(zn)
                ans = ans + Dict[5 * temp] + (zn - 5) * Dict[temp]
            else:
                ans = ans + (10 - zn) * Dict[temp] + Dict[10 * temp]
            num = num % temp
            temp /= 10
        return ans
