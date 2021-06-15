class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        string1=""
        string2=""
        string3=""
        dict={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9}
        for i in firstWord:
            if i in dict:
                string1=string1+str(dict[i])
        string1=int(string1)
        
        for j in secondWord:
            if j in dict:
                string2=string2+str(dict[j])
        string2=int(string2)       

        for k in targetWord:
            if k in dict:
                string3=string3+str(dict[k])
        string3=int(string3)  
      
        
           

        if string1+string2==string3:
            return True
        else:
            return False      
