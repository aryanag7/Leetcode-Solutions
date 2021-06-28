class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[0]*len(boxes)
        for i in range(0,len(boxes)):
            moves=0
            for j in range(0,len(boxes)):
                if boxes[j]=="1":
                    moves+=abs(i-j)
                    ans[i]=moves
        return ans      
