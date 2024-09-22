"""https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=problem-list-v2&envId=string
"""

class Solution(object):
    def letterCombinations(self, digits):
        SLOVAR=['','',"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ans=[]
        s=""
        def S (s,i):
            if(len(s)==len(digits)):
                ans.append(s)
                return
            for j in range (len(SLOVAR[int(digits[i])])):
                s+=SLOVAR[int(digits[i])][j]
                S(s,i+1)
                s=s[:-1]
        S(s,0)
        if(len(ans)==1 and ans[0]==""): ans=[]
        return ans
