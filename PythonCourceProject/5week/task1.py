"""https://leetcode.com/problem-list/hash-table/
url:https://leetcode.com/problems/group-anagrams/"""


class Solution:
    def groupAnagrams(self, strs):
        mp = {}
        for x in strs:
            word = "".join(sorted(x))
            if word in mp:
                mp[word].append(x)
            else:
                mp[word] = [x]
        ans = list(mp.values())
        return ans
