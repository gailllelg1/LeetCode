class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        i,lena,lenb, reset,record = 1,len(a),len(b),0,[]
        while i<=lena or i<=lenb :
            #reset=0
            print("first:"+str(reset))
            temp = reset
            if i<=lena:
                temp += int(a[-i])
                print("a:"+a[-i])
            if i<=lenb:
                temp += int(b[-i])
                print("b:"+b[-i])
            #print("temp:"+str(temp))
            reset = temp/2
            print("secord_reset:"+str(reset))
            record.append(str(temp%2))
            print("record:"+str(record))
            i+=1
            print("\n")
        
        #print(str(i-1)+"wrewe:"+str(reset))    
        if reset:
            record.append(str(reset))
            #print("asdasd")
            
        #print(str(i-1)+"record:"+str(record))
        return ''.join(record[::-1])
