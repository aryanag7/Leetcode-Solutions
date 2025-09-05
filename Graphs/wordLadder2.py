import bisect
import sys
import os
import math
from collections import defaultdict
from collections import Counter
from typing import Deque
from collections import deque
from itertools import accumulate

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Redirect stdin and stdout
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')



class Solution:
    # TC:- its difficult to predict as there can be multiple sequences based on examples but near about previous one + extra

    # TC:- O N * (WORD LEN * 26) 


#   Let’s say there are P total paths enqueued during BFS and the average path length is K.

# Total cost = O(P · K) just from path copying.

# In the worst case, K can be O(N), so the cost can blow up toward O(N²) (or worse if there are exponentially many paths).


    def findLadders(self, beginWord, endWord, wordList):
        uniqueWordList = set(wordList)

        if endWord not in uniqueWordList:
            return []
    
        queue = [[beginWord]]

        usedWords = defaultdict(set)

        ans=[]

        while len(queue)>0:
            li = queue.pop(0)
            lastWord = li[-1] #last word to process
            if lastWord == endWord:
                ans.append(li)
                continue


            currLevel =len(li)

            #near about O(N) OVERALL as there are max n words in the wordlist
            if len(usedWords[currLevel])>0:
                for val in usedWords[currLevel]:
                    uniqueWordList.remove(val)
                
                usedWords[currLevel] = set()



            n= len(lastWord)
            for i in range(0,n):
                for j in range(0,27):
                    newWord = lastWord[:i] + chr(97+j)  + lastWord[i+1:]
                    if newWord in uniqueWordList:
                        queue.append(li+[newWord])
                        usedWords[currLevel+1].add(newWord)
        
        return ans
    

    from collections import deque, defaultdict
    def findLadders(self, beginWord, endWord, wordList):
        uniqueWordList = set(wordList)

        if endWord not in uniqueWordList:
            return []
    
        queue = deque([[beginWord]])

        usedWords = defaultdict(set)

        ans=[]

        shortestLength = None

        while len(queue)>0:
            li = queue.popleft()
            lastWord = li[-1] #last word to process

            if lastWord == endWord:
                ans.append(li)
                if shortestLength is None:
                    shortestLength = len(li)
                continue

            if shortestLength is not None and  len(li)>shortestLength:
                continue


            currLevel =len(li)

            if len(usedWords[currLevel])>0:
                for val in usedWords[currLevel]:
                    uniqueWordList.remove(val)
                
                usedWords[currLevel] = set()



            n= len(lastWord)
            for i in range(0,n):
                for j in range(0,27):
                    if chr(97+j)==lastWord[i]:
                        continue
                    newWord = lastWord[:i] + chr(97+j)  + lastWord[i+1:]
                    if newWord in uniqueWordList:
                        queue.append(li+[newWord])
                        usedWords[currLevel+1].add(newWord)
        
        return ans




                    
      
  






s1 = Solution() 
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(s1.findLadders(beginWord,endWord,wordList))

    


