#import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #return(int(math.sqrt(x)))
        i=0
        if(i==0 and x==0):
            return(0)
        while(i<x):
            i+=1
            if(i*i==x):
                return(i)
            elif(i*i>x):
                return(i-1)
