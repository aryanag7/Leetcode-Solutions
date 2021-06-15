class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        
        
        
            
#             ruleKeys={"type":0,"color":1,"name":2}
#             ans=0
#             for i in items:
#                 if i[ruleKeys[ruleKey]] == ruleValue:
#                     ans += 1
            
#             return ans
  
        ans=0
        for i in items:
            if ruleKey=="type" and i[0] == ruleValue:
                ans=ans+1
            elif ruleKey=="color" and i[1] == ruleValue:
                ans=ans+1
            elif ruleKey=="name" and i[2] == ruleValue:
                ans=ans+1    
        return ans   
