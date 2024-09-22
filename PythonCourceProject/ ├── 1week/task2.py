"""https://leetcode.com/problem-list/string/
https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=problem-list-v2&envId=string
"""

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        p=100000007
        st=s
        lw=len(words)
        l=len(words[0])
        hsum=0
        ans=[]
        if(lw*l>len(s)): return ans
        for i in range(lw):
            hss=0
            if(not(l<2 and lw>1000)):
                for j in range (l):
                    hss=(hss*257+ord(words[i][j]))%p
                hsum=(hsum+hss)%p
            else: 
                for j in range (l):
                    hsum=(hsum*257+ord(words[i][j]))%p
        print(hsum)
        print("fff")
        """print(ord('b'))
        print(ord('b')*257+ord('a'))
        print((ord('b')*257**2+ord('a')*257+ord('r'))%p)"""
        khh=0
        for i in range(len(s)-l*lw+1):
            hh=0
            if(not(l<2 and lw>1000)):
                for j in range(i,i+l*lw,l):
                    "print(j)"
                    hhh=0
                    for (ij) in range(l):
                        hhh=(hhh*257+ord(s[j+ij]))%p
                    hh=(hhh+hh)%p
            else:
                if(i==0):
                    for j in range(i,i+l*lw,l):
                        khh=(khh*257+ord(s[j]))%p
                        hh=khh
                else:
                    khh=((((khh-ord(s[i-1])*(257**(l*lw-1)))*257)%p+ord(s[i+l*lw-1])))%p
                    "print(khh)"
                    hh=khh
            if(hh==hsum): 
                if(l*lw>1000):ans.append(i)
                elif(l<10):
                    fl=1
                    kostil1=[]
                    kostil1.extend(words)
                    for rem in range (i,i+l*lw,l):
                        "print(GGGGGG, s[rem:rem+l])"
                        if(s[rem:rem+l] in kostil1):
                            kostil1.remove(s[rem:rem+l]) 
                            "print(kostil1)"
                        else:
                            fl=0
                            print("pshnh")
                            break
                            
                    if(fl):ans.append(i)
                else: ans.append(i)
        return ans
