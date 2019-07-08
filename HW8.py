class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        F=[0,1]
        #print(F)
        #print(N)
        if N == 0 :
            return(0)
        elif N==1 :
            return(1)
        for i in range(1,N):
            print("i  "+str(i))
            sum=F[-1]+F[-2]
            F.append(sum)
            print(sum)
            print(F)
        print(F[-1])
        return(F[-1])
