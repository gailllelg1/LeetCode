class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        a=num/10
        b=num%10
        num=a+b
        while(num>=10):
            a=num/10
            b=num%10
            num=a+b
        return(num)
