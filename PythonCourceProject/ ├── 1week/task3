"""https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1399003286/?envType=problem-list-v2&envId=string"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        substr=""
        ans=""
        for i in range (0,n):
            if not(s[i]in substr): 
                substr+=s[i]
                if len(substr)>len(ans):
                    ans=substr
            else:
                substr=substr[substr.find(s[i])+1:]
                substr+=s[i]
        return(len(ans))
