class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        for i in range(0,len(prices)):
            stack.append(prices[i])
            for j in range(i+1,len(prices)):
                if stack[-1]>=prices[j]:
                    data=stack[-1]
                    stack.pop()
                    stack.append(data-prices[j])
                    break
      
        return stack
