import bisect
import sys
import os
import math
from collections import defaultdict
from collections import Counter
from typing import Deque
from collections import deque
from itertools import accumulate
import heapq
import time

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Redirect stdin and stdout
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')





# TC:-
# postTweet - O(1) adding a post into the posts dictionary

# getNewsFeed -

"""
Assuming O(U) posts of the user and N followes of this user with M avg posts each

total posts stored for this user:- O(U) + O(N*M) ~ O(M)

loop - O(U) + O(N *M)

sorting :- O(M log M)

"""

# follow - O(1) - adding into the set
# unfollow - O(1) - removing from the set

# SC:-
# O(T) for total tweets posted in posts
# O(P) total number of edges - kind of graph

class Twitter:

    def __init__(self):
        self.followers = defaultdict(set) #list of followers for user
        self.posts = defaultdict(list) # (tweetId, timestamp) for user
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        ts = time.time()
        self.posts[userId].append((tweetId,ts))
        

    def getNewsFeed(self, userId: int):
        allPosts = []
        for tweetId, ts in self.posts[userId]:
            allPosts.append((tweetId,ts))
        
        for followerId in self.followers[userId]:
            for tweetId, ts in self.posts[followerId]:
                allPosts.append((tweetId,ts))
        
        allPosts.sort(key= lambda x:x[1], reverse=True)

        k=10 # 10 posts
        recent_tweets = []
        n= len(allPosts)
        for i in range(min(k,n)):
            tID, ts = allPosts[i]
            recent_tweets.append(tID)
        
        return recent_tweets



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)






# ----------------------------------------------------------------------------


    #optimized over the M log(M) - where M is O(U) + O(N*M) WITH 
    # O(MlogK) and space O(K)

    def getNewsFeed(self, userId: int):
        minHeap = []
        k=10 # 10 posts


        for twID, ts in self.posts[userId]:
            heapq.heappush(minHeap, (ts, twID))
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        
        for followerId in self.followers[userId]:
            for twID, ts in self.posts[followerId]:
                heapq.heappush(minHeap, (ts, twID))
                if len(minHeap)>k:
                    heapq.heappop(minHeap)
    
        minHeap.sort(key= lambda x:x[0],reverse=True)

        recent_tweets = []
        for ts, id in minHeap:
            recent_tweets.append(id)
        return recent_tweets
    





# ----------------------------------------------------------------------------

    
    #optimized over the above solution:- O(F log(F+1)+ O( Klog(F+1)) where F is number of followes for that person

    def getNewsFeed(self, userId: int):
        maxHeap = []
        k=10 # 10 posts

        n = len(self.posts[userId])
        if n>0:
            twID, ts =  self.posts[userId][-1]
            heapq.heappush(maxHeap, (-ts, userId, twID, n-1))

        for followe in self.followers[userId]:
            l = len(self.posts[followe])
            if l>0:
                twID, ts =  self.posts[followe][-1]
                heapq.heappush(maxHeap, (-ts, followe,  twID, l-1))
        
        recent_tweets = []
        for i in range(min(k,len(maxHeap))):
            if not maxHeap: break
            ts, userId, twID, index = heapq.heappop(maxHeap)
            ts=-ts
            recent_tweets.append(twID)

            
            
            prevtWID, prevTs =  self.posts[userId][index-1]
            if index-1 >= 0:
                heapq.heappush(maxHeap, (-prevTs, userId, prevtWID, index-1))
            
        

        return recent_tweets






# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5) # User 1 posts a new tweet (id = 5).
print(obj.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
obj.follow(1, 2);    # User 1 follows user 2.
obj.postTweet(2, 6) # User 2 posts a new tweet (id = 6).
print(obj.getNewsFeed(1))  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
obj.unfollow(1, 2)  # User 1 unfollows user 2.
print(obj.getNewsFeed(1)) #// User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
