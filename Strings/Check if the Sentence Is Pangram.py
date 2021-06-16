class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        mark=[0]*26
        
        for i in range(len(sentence)):
            index=ord(sentence[i])-97
            mark[index]=1
        if 0 not in mark:
            return True
        else:
            return False
