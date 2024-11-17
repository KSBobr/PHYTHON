# https://leetcode.com/problem-list/sliding-window/
# url:https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/?envType=problem-list-v2&envId=sliding-window


class Solution(object):
    def numberOfSubstrings(self, s):
        n = len(s)
        cnt = 0

        Z = [i for i in range(n) if s[i] == "0"]

        if not Z:
            return n * (n + 1) // 2

        Z_ind = 0

        for l in range(n):
            while Z_ind < len(Z) and Z[Z_ind] < l:
                Z_ind += 1

            valid_Z = Z[Z_ind : min(Z_ind + 201, len(Z))] + [n]

            Z_cnt = 0
            last = l

            for ind in valid_Z:
                min_one = Z_cnt * Z_cnt
                min_ind = max(l + min_one + Z_cnt - 1, last)

                if min_ind < ind:
                    cnt += ind - min_ind

                last = ind
                Z_cnt += 1

        return cnt
