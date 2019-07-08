class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        for i in range(0,len(str(x))):
            judge=1
            #print("-i    "+a[-(i+1)])
            #print("i    "+a[i])
            if a[-(i+1)]==a[i]:
                judge=1
                continue
            else:
                judge=0
                break
        print(judge)
        if judge==1:
            return True
