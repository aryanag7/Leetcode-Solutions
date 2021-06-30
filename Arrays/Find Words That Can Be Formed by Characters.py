class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        
        count=Counter(chars)
        sum=0
        for word in words:
            found=True
            new=Counter(word)
            for x in word:
                if new[x]>count[x] or x not in count:
                    found=False
            if found==True:
                sum+=len(word)


        return sum 
        
