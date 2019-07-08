class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        res=[]
        tb=""
        st=""
        space=1
        sw=1
        for i, word in enumerate(S):
            print("word: "+str(word[0]))
            print(space)
            if word[0] in "aeiouAEIOU" and space==1:
                print("asd"+word)
                #res.append(word+"ma"+"a"*(sw))
                st+=word[0]
                
                space=0
            elif word[0]!=" " and space==1:
                tb=word[0]
                space=0
                print("tb "+tb)
            elif word[0]!=" ":
                print("QQQ"+word)
                st+=word[0]
                print(st)
            elif word[0]==" ":
                res.append(st+tb+"ma"+"a"*sw)
                sw+=1
            
            if word[0] ==" ":
                space=1
                print("zxc"+word[0])
                st=""
                tb=""
            else:
                space=0
                
        res.append(st+tb+"ma"+"a"*sw)
        #print("/".join(res))
        return " ".join(res)
