"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-to-integer-atoi/description
"""

class Solution(object):
    def myAtoi(self, s):
        n=len(s)
        ans=0
        zn=1
        zni=0
        znt=0
        startint=0
        endint=0
        if (s==""): return (ans)
        Ch="0123456789"
        for i in range (n):
            if (s[i] in Ch):
                startint=i
                break
            else:
                if(not((s[i]==' ') or s[i]=='-' or s[i]=='+')):
                    return ans
                elif (s[i]=='-' and znt==0): 
                    zn=zn*-1
                    zni=i
                    znt=1
                elif (s[i]=='+' and znt==0): 
                    zni=i
                    znt=1
        if(znt and zni+1!=startint):return(ans)                                      
        if (startint==0  and not(s[0] in Ch)):return (ans)          
        for i in range (startint,n):
            if(not(s[i]in Ch)):
                endint=i
                break    
        
        if (endint==0): 
            endint=n
        ch=s[startint:endint]
        print(startint,endint)
        print(ch)
        ans=int(ch)*zn
        if(ans<-2**31):ans=-2**31
        if(ans>2**31-1): ans=2**31-1
        return (ans)
