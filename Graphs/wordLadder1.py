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
    def ladderLength(self, beginWord, endWord, wordList):
        uniqueWordList = set(wordList)
        # processedWords = set()
        if endWord not in uniqueWordList:
            return 0
        
        queue = [(beginWord,1)]
        while len(queue)>0:
            word , steps = queue.pop(0)
            if word == endWord:
                return steps


            # TC:- O N * (WORD LEN * 26) 
            n=len(word)
            for i in range(0,n):
                for j in range(0,27):
                    newWord = word[:i] + chr(97+j)  + word[i+1:]
                    if newWord in uniqueWordList:
                        queue.append((newWord,steps+1))
                        uniqueWordList.remove(newWord)
        return 0







s1 = Solution() 
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(s1.ladderLength(beginWord,endWord,wordList))

    


