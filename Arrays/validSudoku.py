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
    # TC:- O(9X9)
    # SC:- O(9 row x 9 ele) + O(9 cols x 9 ele) + O(9 sub matrix x 9 ele) ~ n^2


    """
    if a board is 16x16 ie n=16, each row can have 
    """
    def isValidSudoku(self, board):
        rowSet = [set() for i in range(9)]
        colSet = [set() for j in range(9)]
        boxSet = [set() for k in range(9)]

        for i in range(0,9):
            for j in range(0,9):
                num = board[i][j]
                
                if num==".":
                    continue

                box_index = (i//3*3)+j//3

                if num in rowSet[i] or num in colSet[j] or num in boxSet[box_index]:
                    return False
                
                rowSet[i].add(num)
                colSet[j].add(num)

             
                # print(box_index, (i,j))
                boxSet[box_index].add(num)
        
        return True









s1 = Solution()
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(s1.isValidSudoku(board))
    

