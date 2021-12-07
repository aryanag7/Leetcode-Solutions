#Python Approach 1 Using 2 dictionary

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        for i in nums1:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        dict2={}
        for i in nums2:
            if i in dict2:
                dict2[i]+=1
            else:
                dict2[i]=1
        ans=[]
        for i in dict1:
            if i in dict2:
                ans.append(i)
        return ans
#Approach 2 Binary Search 
import bisect
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        ans=[]
        for i in nums1:
          
            index=bisect.bisect_left(nums2,i)
            if index!=len(nums2) and nums2[index] not in ans and i==nums2[index]:
                ans.append(nums2[index])
        return ans
#Approach 3 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicty={}
        for i in nums1:
            if i in dicty:
                dicty[i]+=1
            else:
                dicty[i]=1
        ans=[]
        for i in nums2:
            if i in dicty and i not in ans:
                ans.append(i)
        return ans
        
        
        
