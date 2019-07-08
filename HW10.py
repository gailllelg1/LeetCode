class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        #print(len(A))
        print(A)
        a=[]
        for i in range(len(A)):
            if i%2 != 1 and A[i]%2==1 :
                a.append(i)
                print(A[i])
        print(a)
        j=0
        for i in range(len(A)):
            if i%2 == 1 and A[i]%2!=1:
                st = A[i]
                print(A[i])
                print(A[a[j]])
                A[i] = A[a[j]]
                A[a[j]] = st
                j+=1
        #print(A)
        return(A)
