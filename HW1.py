class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2**31-1 or x <= -2**31:
            return int(0)
        else:
            s = cmp(x,0)#用x去跟0比 判斷正負 x>0回傳1 x==0 回傳0 x<0回傳-1
            num=0
            x=abs(x)
            while x>0:
                #print(x)
                num = num*10+x%10
                x=x/10
            if num >= 2**31-1 or num <= -2**31:
                return int(0)
            else:
                return int(num*s)
