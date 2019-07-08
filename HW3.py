class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        rt=0
        st=0
        space=0
        for i in range(len(s)):
            #rt+=1
            
            if s[i]==" " and i==len(s)-1:
                #rt-=1
                continue
            elif s[i]==" " and space==1:
                continue
            elif s[i]==" ":
                space=1
                st=rt
                rt=0
            else:
                rt+=1
                st=rt
                space=0
        return(st)
        
